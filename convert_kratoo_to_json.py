import json
import requests

lines = open("review_tags_thai.txt",'r').read().splitlines()
completed_data = []
count = 0

for kratoo in lines:
    url = requests.get("https://ptdev03.mikelab.net/kratooc/" + str(kratoo))
    content_json = json.loads(url.text)
    completed_data.append(content_json)
    count += 1
    print(count)
with open('completed_data.json', 'w') as outfile:
    json.dump(completed_data, outfile)

