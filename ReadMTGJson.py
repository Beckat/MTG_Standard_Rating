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
f = open('AtomicCards.json', encoding='utf-8-sig')

# returns JSON object as
# a dictionary
data = json.load(f)
#cards = data["data"]
#card_test_df = pd.DataFrame

#card_holder = []
#mana_cost = ""

#all_cards_export = pd.read_json("StandardAtomic.json", orient = "index")

#ruin_crab = data["data"]["Angel of Destiny"][0]["name"]
#card_face_name = None

Environment = Env.Environment()
engine = Environment.get_database_engine()
Session = sessionmaker(bind=engine)
s = Session()

for card in data["data"]:
    card_name = data["data"][card][0]["name"]
    if "faceName" in data["data"][card][0]:
        card_face_name = data["data"][card][0]["faceName"]
    else:
        card_face_name = data["data"][card][0]["name"]

    card_type = data["data"][card][0]["type"]

    if "toughness" in data["data"][card][0]:
        if data["data"][card][0]["toughness"].isnumeric():
            card_toughness = data["data"][card][0]["toughness"]
        else:
            card_toughness = 0.0
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
        if data["data"][card][0]["power"].isnumeric():
            card_power = data["data"][card][0]["power"]
        else:
            card_power = 0.0
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
    if "legalities" in data["data"][card][0]:
        card_legalities = str(data["data"][card][0]["legalities"])
    else:
        card_legalities = None
    if "keywords" in data["data"][card][0]:
        card_keywords = data["data"][card][0]["keywords"]
    else:
        card_keywords = None
    if "identifiers" in data["data"][card][0]:
        card_identifiers = str(data["data"][card][0]["identifiers"])
    else:
        card_identifiers = None
    if "hasAlternativeDeckLimit" in data["data"][card][0]:
        card_alternative_deck_limit = data["data"][card][0]["hasAlternativeDeckLimit"]
    else:
        card_alternative_deck_limit = None
    if "faceConvertedManaCost" in data["data"][card][0]:
        card_face_converted_mana_cost= data["data"][card][0]["faceConvertedManaCost"]
    else:
        card_face_converted_mana_cost = None

    if "edhrecRank" in data["data"][card][0]:
        card_ehdrec_rank = data["data"][card][0]["edhrecRank"]
    else:
        card_ehdrec_rank = None
    if "convertedManaCost" in data["data"][card][0]:
        card_converted_mana_cost = data["data"][card][0]["convertedManaCost"]
    else:
        card_converted_mana_cost = None
    if "colors" in data["data"][card][0]:
        card_colors = data["data"][card][0]["colors"]
    else:
        card_colors = None
    if "colorIndicator" in data["data"][card][0]:
        card_color_indicator = data["data"][card][0]["colorIndicator"]
    else:
        card_color_indicator = None
    if "colorIdentity" in data["data"][card][0]:
        card_color_identity = data["data"][card][0]["colorIdentity"]
    else:
        card_color_identity = None
    if "asciiName" in data["data"][card][0]:
        card_ascii_name = data["data"][card][0]["asciiName"]
    else:
        card_ascii_name = None
    if "types" in data["data"][card][0]:
        card_types = data["data"][card][0]["types"]
    else:
        card_types = None

    add_card = Card(name=card_name, faceName=card_face_name, type=card_type, toughness=card_toughness,
                    text=card_text, supertypes=card_supertypes, subtypes=card_subtypes,
                    side=card_side, printings=card_printings, power=card_power, manaCost=card_mana_cost,
                    loyalty=card_loyalty, life=card_life, legalities=card_legalities, keywords=card_keywords,
                    identifiers=card_identifiers, hasAlternativeDeckLimit=card_alternative_deck_limit,
                    faceConvertedManaCost=card_face_converted_mana_cost, edhrecRank=card_ehdrec_rank,
                    convertedManaCost=card_converted_mana_cost, colors=card_colors, colorIndicator=card_color_indicator,
                    colorIdentity=card_color_identity, asciiName=card_ascii_name, types=card_types)
    s.add(add_card)
    try:
        s.commit()
    except IntegrityError:
        s.rollback()

s.close()


