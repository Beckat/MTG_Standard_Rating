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
    colors = Column(String)
    faceName = Column(String)
    manaCost = Column(String)

    def __repr__(self):
        return """""""<Card(name='{}', colors='{}', faceName='{}'," \
               "manaCost='{}'>""" \
            .format(self.name, self.colors, self.faceName, self.manaCost)


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

card = Card(name=ruin_crab, colors=data["data"]["Angel of Destiny"][0]["colors"], faceName=None,manaCost=data["data"]["Angel of Destiny"][0]["manaCost"])

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


