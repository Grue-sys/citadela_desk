import csv
from random import choice, random

def all_characters_deck():
    with open("citadela_table_characters.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        all_character_type = [row for row in reader]
        return all_character_type


def in_game_characters(all_characters):
    game_characters = []
    temp_char = []
    used_ranks = []


    while len(game_characters) < 9:
        while len(temp_char) < 3:
            for line in all_characters:
                if temp_char["rank"] not in used_ranks:
                    temp_char.append(line)
        game_characters.append(choice(temp_char))
        used_ranks.append(temp_char["rank"])
        temp_char.clear()
    return game_characters


all_characters = all_characters_deck()
game_characters = in_game_characters(all_characters)

print(all_characters["rank"])

for character in all_characters:
    print(character)

print(f"-" * 80)

for character in game_characters:
    print(character)

#TODO - check & fix





"""
    while len(game_characters) > 9:
        temp_characters = [char for char in all_characters if char["rank"] not in used_ranks]
        print(temp_characters)
        temp_character = choice(all_characters)
        game_characters.append(temp_character)
        used_ranks.add(temp_character['rank'])

def in_game_characters(all_characters):
    temp_characters = []
    game_characters = []
    for line in all_characters:
        if int(len(line["rank"])) == 0 or int(len(line["rank"])) < 2:
            temp_characters.append(line)
        temp_character = choice(temp_characters)
        game_characters.append(temp_character)
        temp_characters.clear()
    return game_characters







for character in all_characters:
    print(character)
"""
