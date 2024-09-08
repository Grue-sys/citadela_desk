import csv
from random import choice


class CSVLoader:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def load(self):
        try:
            with open(self.csv_file, encoding="utf-8", mode="r") as f:
                reader = csv.DictReader(f)
                cards = []
                for row in reader:
                    cards.append(row)
                return cards

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error when loading file {self.csv_file}: {e}")


class DistrictsDeckBuilder:
    @staticmethod
    def all_districts(unique_districts):
        all_districts = []
        for card in unique_districts:
            for i in range(int(card["quantity"])):
                all_districts.append({
                    "Name": card["name_orig"],
                    "Color": card["color"],
                    "Cost": int(card["cost"]),
                    "Note": card["note_orig"],
                    "Vanila": bool(card["vanila_game"])
                })
        return all_districts

    @staticmethod
    def make_districts_deck(all_districts):
        purple_cards = []
        game_deck = []
        for card in all_districts:
            if card["Color"] != "Purple":
                game_deck.append(card)
            else:
                purple_cards.append(card)
        for i in range(15):
            random_purple = choice(purple_cards)
            game_deck.append(random_purple)
            purple_cards.remove(random_purple)
        return game_deck


class CharactersDeckBuilder:
    @staticmethod
    def all_characters(characters):
        all_characters = []
        for card in characters:
            all_characters.append({
                "Rank": int(card["rank"]),
                "Name": card["name_orig"],
                "Color": card["color"],
                "Vanila": bool(card["vanila_game"])
            })
        return all_characters


    @staticmethod
    def random_characters(all_characters):
        game_characters = []
        for i in range(1, 10):
            character_rank = [character for character in all_characters if character["Rank"] == i]
            if character_rank:
                random_character = choice(character_rank)
                game_characters.append(random_character)
        return game_characters


#Districts deck builder
districts_load = CSVLoader("citadela_table_districts.csv").load() #loading .csv
all_districts_cards = DistrictsDeckBuilder.all_districts(districts_load) #creates all districts cards
game_deck_districts = DistrictsDeckBuilder.make_districts_deck(all_districts_cards) #makes game card desk of districts

#Characters builder
characters_load = CSVLoader("citadela_table_characters.csv").load() #loading .csv
all_characters_cards = CharactersDeckBuilder.all_characters(characters_load) #creates all available characters
random_game_characters = CharactersDeckBuilder.random_characters(all_characters_cards) #choose random 1 character/rank


if __name__ == "__main__":
    for line in all_districts_cards:
        print(line)
    print(len(all_districts_cards))

    print(f"-" * 120)

    for line in game_deck_districts:
        print(line)
    print(len(game_deck_districts))

    print(f"*" * 120)

    for line in all_characters_cards:
        print(line)
    print(len(all_characters_cards))

    print(f"-" * 120)

    for line in random_game_characters:
        print(line)
    print(len(random_game_characters))