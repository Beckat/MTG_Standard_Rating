import json
import pandas as pd

# Opening JSON file
f = open('AtomicCards.json', )

# returns JSON object as
# a dictionary
data = json.load(f)
cards = data["data"]

all_cards_export = pd.read_json("AtomicCards.json", orient = "index")
all_cards_transpose = all_cards_export.transpose()
#all_cards_next = pd.DataFrame(all_cards_export.data)
print(all_cards_export.head())
print("HOLD")
print(all_cards_export.columns)

print(all_cards_transpose.head())
print("HOLD")
print(all_cards_transpose.columns)
all_cards_next_2 = all_cards_next.data.apply(lambda x: pd.read_json(json.dumps(x), orient = "records"))
all_cards = all_cards_export.data.apply(lambda x: pd.read_json(json.dumps(x), orient = "name"))

# Iterating through the json
# list
for card in cards.items():
    print(card)
    print(card["manacost"])


# Closing file
f.close()