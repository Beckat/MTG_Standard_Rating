import json
import pandas as pd
import sqlalchemy as sqlal
from sqlalchemy.orm import sessionmaker
import Env
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.exc import IntegrityError

Base = declarative_base()


class ReadCards:
    def __init__(self):
        self.card = None


class Card(Base):
    __tablename__ = 'MTG Cards'
    name = Column(String, primary_key=True)
    type = Column(String)
    toughness = Column(sqlal.FLOAT)
    text = Column(String)
    supertypes = Column(String)
    subtypes = Column(String)
    side = Column(String)
    printings = Column(String)
    power = Column(sqlal.FLOAT)
    manaCost = Column(String)
    loyalty = Column(String)
    life = Column(sqlal.FLOAT)
    legalities = Column(String)
    keywords = Column(String)
    identifiers = Column(String)
    hasAlternativeDeckLimit = Column(String)
    faceName = Column(String)
    faceConvertedManaCost = Column(String)
    edhrecRank = Column(String)
    convertedManaCost = Column(sqlal.FLOAT)
    colors = Column(String)
    colorIndicator = Column(String)
    colorIdentity = Column(String)
    asciiName = Column(String)
    types = Column(String)

    def __repr__(self):
        return """""""<Card(name='{}', colors='{}', faceName='{}'," \
               "manaCost='{}'>""" \
            .format(self.name, self.type, self.toughness,
                    self.text, self.subtypes, self.subtypes,
                    self.side, self.printings, self.power, self.manaCost,
                    self.loyalty, self.life, self.legalities, self.keywords,
                    self.identifiers, self.hasAlternativeDeckLimit, self.faceName,
                    self.faceConvertedManaCost, self.edhrecRank, self.convertedManaCost,
                    self.colors, self.colorIdentity, self.asciiName, self.types)


card_reader = ReadCards()

# Opening JSON file
f = open('StandardAtomic.json', encoding='utf-8-sig')

# returns JSON object as
# a dictionary
data = json.load(f)
cards = data["data"]
card_test_df = pd.DataFrame

card_holder = []
mana_cost = ""

all_cards_export = pd.read_json("StandardAtomic.json", orient = "index")

ruin_crab = data["data"]["Angel of Destiny"][0]["name"]

card = Card(name=ruin_crab, toughness=data["data"]["Angel of Destiny"][0]["toughness"], colors=data["data"]["Angel of Destiny"][0]["colors"], faceName=None,manaCost=data["data"]["Angel of Destiny"][0]["manaCost"], type=data["data"]["Angel of Destiny"][0]["type"], types=data["data"]["Angel of Destiny"][0]["types"])

Environment = Env.Environment()
engine = Environment.get_database_engine()
Session = sessionmaker(bind=engine)
s = Session()
s.add(card)
try:
    s.commit()
except IntegrityError:
    s.rollback()
s.close()


