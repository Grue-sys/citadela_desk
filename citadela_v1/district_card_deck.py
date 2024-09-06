from random import choice, shuffle
import csv
import copy


#.csv loader & single (unique cards generator)
def csv_loader():
    district_type = []
    try:
        with open("citadela_table_districts.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                district_type.append(row)
            return district_type

    except FileNotFoundError:
        return f"File not found."
    except Exception as e:
        return f"Error: {e}."

# multiplying cards based on "quantity" column value
def multiply_cards(unique_cards):
    all_districts = []
    for line in unique_cards:
        for i in range(int(line["quantity"])):
            all_districts.append({
                "name": line["name_orig"],
                "color": line["color"],
                "cost": line["cost"],
                "note": line["note_orig"]
            })
    return all_districts

# deck contains all basic (non-purple) cards & 15 random purple cards
def deck_builder(all_districts):
    game_cards = []
    legendary_cards = []
    for line in all_districts:
        if line["color"] != "Purple":
            game_cards.append(line)
        elif line["color"] == "Purple":
            legendary_cards.append(line)
    for i in range(15):
        random_legendary = choice(legendary_cards)
        game_cards.append(random_legendary)
        legendary_cards.remove(random_legendary)
    return game_cards

def deck_shuffle(card_deck):
    shuffle(card_deck)



# csv_loader sends raw info about each card -> multiply creates relevant amount of copy in proper format (dict)
all_cards = multiply_cards(csv_loader())
# from all cards sorted basic cards & 15 special one
districts_card_deck = deck_builder(all_cards)
# deepcopy made for shuffle, original stays for overview
game_deck = copy.deepcopy(districts_card_deck)




if __name__ == "__main__":
    for card in districts_card_deck:
        print(f"Karta: {card}", end="\n")
    print(len(districts_card_deck))
    print(f"-" * 80)

    deck_shuffle(game_deck)
    for card in game_deck:
        print(f"Karta: {card}", end="\n")
    print(len(game_deck))