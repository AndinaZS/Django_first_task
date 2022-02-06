import csv
import json


def converting(csv_file, json_file):
    lst_data = []
    with open('datasets/'+ csv_file, encoding='utf-8') as csv_f:
        data = csv.DictReader(csv_f)
        for rows in data:
            lst_data.append(rows)

    with open('datasets/'+ json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(lst_data))


converting('categories.csv', 'categories.json')
converting('ads.csv', 'ads.json')