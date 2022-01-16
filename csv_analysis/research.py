"""
Read CSV database, parse and clean the DATA ti be used
"""
import csv
import os


def read_csv():
    """
    read csv database in data dir
    """
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, "data", "drinks.csv")

    with open(file_name, "r") as f:
        print(f.read())