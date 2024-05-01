import csv

CSV_PATH = "./tests/csv/success_message.csv"


def success_message():
    success_dict = dict()
    with open(CSV_PATH, 'r', encoding='utf-8') as file:
        success = csv.DictReader(file)
        for el in success:
            success_dict[el['NAME']] = el['VALUE']
    return success_dict




