import pandas as pd
import json

with open('../Data_files/similar_sectors.json', 'r', encoding='utf-8') as f:
    similar = json.load(f)

df = pd.read_csv('../Data_files/VacData/all_professions.csv')

arr = []

for i, r in df.iterrows():
    profession = r['Professions']
    sector = r['Sector/Industry'].strip()
    if len(sector) > 0:
        sector = similar[sector]
        arr.append([profession, [sector]])

out = pd.DataFrame(arr, columns=['professions', 'sectors'])
out.to_csv('../Data_files/generalized_sectors.csv', index=False)
