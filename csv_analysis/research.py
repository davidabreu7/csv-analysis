"""
Read CSV database, parse and clean the DATA to be used
"""
import csv
import os
from collections import namedtuple


Record = namedtuple(
    "Record",
    "country,beer_servings,spirit_servings,wine_servings,total_litres_of_pure_alcohol",
)


def read_csv():
    """
    read csv database in data dir
    """
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, "data", "drinks.csv")

    with open(file_name, "r") as f:
        csv_dict_list = csv.DictReader(f)

        return [parse_csv(row) for row in csv_dict_list]


def parse_csv(csv_dict: dict) -> namedtuple:
    """
    receives a csv dict, convert the types and return a named tuple
    """

    for key, cell in csv_dict.items():
        if "." in cell and cell.replace(".", "", 1).isdigit():
            csv_dict[key] = float(cell)
        elif csv_dict[key].isdigit():
            csv_dict[key] = int(cell)

    return Record(**csv_dict)


def top_beer(data):
    return sorted(data, key=lambda r: r.beer_servings, reverse=True)


def top_spirit(data):
    return sorted(data, key=lambda r: r.spirit_servings, reverse=True)


def top_wine(data):
    return sorted(data, key=lambda r: r.wine_servings, reverse=True)


def top_alcohol(data):
    return sorted(data, key=lambda r: r.total_litres_of_pure_alcohol, reverse=True)
