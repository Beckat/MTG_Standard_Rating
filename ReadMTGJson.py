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
    faceName = Column(String, primary_key=True)
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
card_face_name = None

for card in data["data"]:
    card_name = data["data"][card][0]["name"]
    if "faceName" in data["data"][card][0]:
        card_face_name = data["data"][card][0]["faceName"]
    else:
        card_face_name = data["data"][card][0]["name"]
    card_type = data["data"][card][0]["type"]
    if "toughness" in data["data"][card][0]:
        card_toughness = data["data"][card][0]["toughness"]
    else:
        card_toughness = None
    if "text" in data["data"][card][0]:
        card_text = data["data"][card][0]["text"]
    else:
        card_text = None
    card_supertypes = data["data"][card][0]["supertypes"]
    card_subtypes = data["data"][card][0]["subtypes"]
    if "side" in data["data"][card][0]:
        card_side = data["data"][card][0]["side"]
    else:
        card_side = None
    if "printings" in data["data"][card][0]:
        card_printings = data["data"][card][0]["printings"]
    else:
        card_printings = None
    if "power" in data["data"][card][0]:
        card_power = data["data"][card][0]["power"]
    else:
        card_power = None
    if "manaCost" in data["data"][card][0]:
        card_mana_cost = data["data"][card][0]["manaCost"]
    else:
        card_mana_cost = None
    if "loyalty" in data["data"][card][0]:
        card_loyalty = data["data"][card][0]["loyalty"]
    else:
        card_loyalty = None
    if "life" in data["data"][card][0]:
        card_life = data["data"][card][0]["life"]
    else:
        card_life = None

card = Card(name=ruin_crab, faceName=card_face_name, toughness=data["data"]["Angel of Destiny"][0]["toughness"], colors=data["data"]["Angel of Destiny"][0]["colors"], type=data["data"]["Angel of Destiny"][0]["type"], types=data["data"]["Angel of Destiny"][0]["types"])

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


