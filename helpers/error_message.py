import csv

CSV_PATH = "./csv/error_message.csv"


def error_message():
    error_dict = dict()
    with open(CSV_PATH, 'r', encoding='utf-8') as file:
        error = csv.DictReader(file)
        for el in error:
            error_dict[el['NAME']] = el['VALUE']
    return error_dict
