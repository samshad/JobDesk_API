import pandas as pd
from langdetect import detect
import json


# df = pd.read_csv('Data/train_occupations_de.csv')
# arr = []
# for i in df['description']:
#     arr.append(detect(i))
#
# print(set(arr))

with open('Data/VacData/S2/vacdata_6.json5', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.json_normalize(data)
print(df.head())
df.to_csv('Data/Dataset/jobtitle_profile6.csv', index=False)
