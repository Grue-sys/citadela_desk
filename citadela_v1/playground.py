import csv
from abc import ABC


class Districts(ABC):
    def __init__(self, color, name, quantity, cost, note):
        self.color = color
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.note = note

    def __repr__(self):
        return f"Districts({self.color}, {self.name}, {self.quantity}, {self.cost}, {self.note})"


class CSVLoader:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def load(self):
        try:
            with open(self.csv_file, mode="r", encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    districts_list.append(Districts(row[0], row[1], row[3], row[4], row[6]))

                for district_type in districts_list:
                    print(district_type)


        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error when loading file: {e}")


class DistrictsFactory(Districts):
    @staticmethod
    def make_card(color, name, quantity, cost, note):
        return Districts(color, name, quantity, cost, note)





loader = CSVLoader("citadela_table_districts.csv")
loader.load()

print(f"-" * 80)
