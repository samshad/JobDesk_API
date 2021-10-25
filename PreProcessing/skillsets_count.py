import pandas as pd
import json
from collections import Counter


skills = []

for id in range(1, 8):
    file = f'Data/VacData/S2/vacdata_{id}.json5'

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(len(data))

    for i in data:
        for p in i['Profiles']:
            for s in p['Skills']:
                # x = ' '.join(s.split()).lower()
                x = s.split(',')
                for xx in x:
                    y = ''.join(xx.split()).lower()
                    if len(y) > 0:
                        skills.append(y)

for id in range(8, 21):
    file = f'Data/VacData/S3/vacdata_{id}.json'

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(len(data))

    for i in data:
        for p in i['Profiles']:
            for s in p['Skills']:
                # x = ' '.join(s.split()).lower()
                x = s.split(',')
                for xx in x:
                    y = ''.join(xx.split()).lower()
                    if len(y) > 0:
                        skills.append(y)

skills_cnt = Counter(skills)
print(skills_cnt)

# df = pd.DataFrame.from_dict(skills_cnt, orient=['skill', 'count'])
df = pd.DataFrame.from_records(skills_cnt.most_common(), columns=['skill', 'count'])
print(df.head())
df.to_csv('Data/Dataset/skillsets.csv', index=False)

# with open('Data/Dataset/skillsets.json', 'w') as f:
#     json.dump(skills_cnt, f, indent=4)
