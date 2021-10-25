import json
import pandas as pd


path = f'Data/VacData/sample-il.txt'

file = open(path, 'r')
lines = file.readlines()

arr = []

for line in lines:
    data = json.loads(line)

    occupation = data['occupation']
    summery = data['summary']
    texts = ''

    for e in data['experiences']:
        texts += (e['title'] + ' ') if e['title'] is not None else ''
        texts += (e['description'] + ' ') if e['description'] is not None else ''

    for i in data['education']:
        tmp = i['degree_name']
        texts += (i['degree_name'] + ' ') if i['degree_name'] is not None else ''
    texts = str(' '.join(texts.split()))
    summery = str(' '.join(summery.split())) if summery is not None else ''
    occupation = str(' '.join(occupation.split())) if occupation is not None else ''

    if len(str(texts + summery)) > 10 and len(occupation) > 0:
        arr.append([texts, summery, occupation])

df = pd.DataFrame(arr, columns=['text', 'summery', 'occupation'])
df.to_csv('Data/Dataset/linkedin_proflies.csv', index=False)
