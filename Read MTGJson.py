import json
import pandas as pd
import sqlalchemy as sqlal
from sqlalchemy.orm import sessionmaker
import Env
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.exc import IntegrityError

Base = declarative_base()


class Card(Base):
    __tablename__ = 'MTG Cards'
    name = Column(String, primary_key=True)
    colors = Column(String)
    faceName = Column(String)
    manaCost = Column(String)

    def __repr__(self):
        return """""""<Book(name='{}', colors='{}', faceName='{}'," \
               "manaCost='{}'>""" \
            .format(self.name, self.colors, self.faceName, self.manaCost)


# Opening JSON file
f = open('StandardAtomic.json', encoding='utf-8-sig')

# returns JSON object as
# a dictionary
data = json.load(f)
cards = data["data"]
card_test_df = pd.DataFrame

card_holder = []

all_cards_export = pd.read_json("StandardAtomic.json", orient = "index")

for card in data["data"]:
    test = card
    test_card = data["data"][card]
    colors = ""
    #print(test_card[0]["name"])
    if len(test_card[0]["colors"]) == 0:
        colors = ""
    else:
        if "W" in str(test_card[0]["colors"]):
            colors = colors + "W"
        if "U" in str(test_card[0]["colors"]):
            colors = colors + "U"
        if "B" in str(test_card[0]["colors"]):
            colors = colors + "B"
        if "R" in str(test_card[0]["colors"]):
            colors = colors + "R"
        if "G" in str(test_card[0]["colors"]):
            colors = colors + "G"
    #print(colors)
    colors = ""

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

