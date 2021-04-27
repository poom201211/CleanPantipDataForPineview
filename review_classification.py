import requests
import json

# select from tags
kratoo_notuse = []
lines = open("clean_data.txt", "r").read().splitlines()
count = 0
for kratoo in lines:
    url = requests.get("https://ptdev03.mikelab.net/kratooc/" + str(kratoo))
    content_json = json.loads(url.text)
    try:
        tags = content_json["_source"]["tags"]
        kratoo_type = content_json["_source"]["type"]
        if(kratoo_type == 4):
            f = open("review_tags_thai.txt", "a")
            f.write(kratoo + '\n')
            count += 1
            print(count)
    except (KeyError, ValueError) as error:
        kratoo_notuse.append(kratoo)

print("tag finished")