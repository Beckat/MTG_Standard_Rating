import json
import pandas as pd
import sqlalchemy as sqlal
from sqlalchemy.orm import sessionmaker
import Env


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
    print(test_card[0]["name"])
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
    print(colors)
    colors = ""

ruin_crab = data["data"]["Ruin Crab"][0]["name"]
print(ruin_crab["name"])

Environment = Env.Environment()
engine = Environment.get_database_engine()
Session = sessionmaker(bind=engine)
s = Session()
#s.add(name=ruin_crab)
s.commit()
s.close()

