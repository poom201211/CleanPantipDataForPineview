import urllib.parse
import json
from pymongo import MongoClient
from datetime import datetime

# --Edit your configuration here ------------------------------
username = urllib.parse.quote_plus('pantip_data')
password = urllib.parse.quote_plus('mikelab4r3e2w1q')
auth_db = urllib.parse.quote_plus('admin')
server = urllib.parse.quote_plus('mars.mikelab.net')
port = urllib.parse.quote_plus('50001')
# -------------------------------------------------------------
client = MongoClient(f"mongodb://{username}:{password}@{server}:{port}/?authSource={auth_db}")
db = client['pantip_clickstream']

# f = open('review_all.txt','a')

for month in range(4, 5):
    review_id = []
    f = open(f'review_{month:02}.txt', 'w')

    for day in range(1, 32):
        cursor = db[f'click-2021{month:02}{day:02}'].find({"rooms": "BP"})
        print(f'click-2021{month:02}{day:02}')
        for record in cursor:
            try:
                for i in record["tags"]:
                    if (
                            i == "เที่ยวไทย" or i == "สถานที่ท่องเที่ยวในประเทศ" or i == "สถานที่ท่องเที่ยวกรุงเทพฯ" or i == "ประเทศไทย" or
                            i == "คาเฟ่ (Cafe)" or i == "ร้านกาแฟ" or i == "ร้านอาหาร" or i == "อาหาร" or i == "อาหารคาว" ):
                        if (record['topic_id'] not in review_id):
                            review_id.append(record['topic_id'])
            except KeyboardInterrupt:
                raise
            except:
                pass

    f.write(str(review_id))
    f.write('\n')

    f.close()
