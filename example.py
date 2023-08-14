from pymongo import MongoClient 
import pandas as pd
import json

client = MongoClient('mongodb://localhost:27017/')

db = client['shop']

collection = db['clothing']

pipeline = collection.aggregate([])

data = json.dumps(list(pipeline))

df = pd.read_json(data)

data_json = df.groupby('item')['sizes']
 
for idx, datax in data_json:
    print('__________',idx,'__________')
    print(datax)
    