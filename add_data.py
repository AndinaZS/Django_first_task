import requests
import json

url = "http://127.0.0.1:8000/cat/"

with open('datasets/categories.json', encoding='utf-8') as json_f:
  for elem in json.load(json_f):
    response = requests.request("POST", url, data=json.dumps(elem))

url = "http://127.0.0.1:8000/ads/"

with open('datasets/ads.json', encoding='utf-8') as json_f:
  for elem in json.load(json_f):
    if elem['is_published'].lower() == "true":
      elem['is_published'] = True
    else:
      elem['is_published'] = False
    response = requests.request("POST", url, data=json.dumps(elem))