import json
import pandas as pd

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
    if len(test_card[0]["colors"]) == 0:
        colors = ""
    else:
        for color in test_card[0]["colors"]:
            colors = colors + color
    print(colors)
    colors = ""

ruin_crab = data["data"]["Ruin Crab"]

all_cards_export = all_cards_export.drop("meta")
all_cards_transpose = all_cards_export.transpose()
#all_cards_next = pd.DataFrame(all_cards_transpose.data)

all_cards_export.head()

for card in all_cards_export.items():
    if "colorIdentity" in str(card[1]) and not card[1] is None:
        test = card[1]
        card_holder.append(card[1])

card_holder_df = pd.DataFrame(card_holder)
card_holder = []

#i = card_holder_df.index.get_loc("date")
#card_holder_df.drop(index="date")
#card_holder_df.drop("")

for i in range(len(card_holder_df)):
    card_holder.append(pd.io.json.json_normalize(card_holder_df.data[i]))
#for row in pd.io.json.json_normalize(card_holder_df.data[0]):
#    card_holder.append(row)
test = pd.io.json.json_normalize(card_holder_df.data[0])

has_first_row = False
for card in card_holder:
    if not has_first_row:
        card_test_df = card
        has_first_row = True
    else:
        card_test_df.append(card, ignore_index=True, sort=False)

cards_df = pd.DataFrame(card_holder)

print("Hold for debug")

print("Middle")
'''
for card in all_cards_transpose:
    if not card == "data":
        data, card = card.split('[')
    print(card)

split_cards = pd.DataFrame(all_cards_transpose.row.str.split(',', 1).tolist(),
                           columns=['title', 'card'])

all_cards_next_2 = pd.DataFrame(all_cards_next.items())
print(all_cards_next_2.head())
print("HOLD")
print(all_cards_next_2.columns)
all_cards_next_3 = all_cards_next_2[1]

all_cards_next_4 = pd.DataFrame(all_cards_next_2[0].tolist()).set_index(all_cards_next_2[1])

card_json = all_cards_next.items()


print("Card Json")
print(card_json)
print("Card Json")

all_cards = json.load(card_json)

print(all_cards_next_2.head())
print("HOLD")
print(all_cards_next_2.columns)
print(all_cards_next_3.head())
print("HOLD")
print(all_cards_next_3.columns)
all_cards_next_2 = all_cards_next_2.data.apply(lambda x: pd.read_json(json.dumps(x), orient = "index"))
all_cards = all_cards_export.data.apply(lambda x: pd.read_json(json.dumps(x), orient = "name"))

# Iterating through the json
# list
for card in cards.items():
    print(card)
    print(card["manacost"])

'''
# Closing file
f.close()
