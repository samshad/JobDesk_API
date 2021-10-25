import pandas as pd
import json
import requests


df = pd.read_csv('../Data/Scraped_data/list.csv')

for i, r in df.iterrows():
    name = r['name']
    name = name.replace('/', '_')
    res = requests.get(f'https://www.jobs.ch/api/v1/public/meta/typeahead?limit=5000&query={name}')
    print(res.status_code)
    data = json.loads(res.content)
    tf = pd.json_normalize(data)
    tf.to_csv(f'JobsChApi/{name}.csv', index=False)

