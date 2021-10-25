import os
import pandas as pd
import ast

df = pd.read_csv('../Data/Scraped_data/combined_csv.csv')
files = os.listdir('../Data/Scraped_data/JobsChApi')

arr = []

c = 0
for i, r in df.iterrows():
    alternatives_names = []
    p = r['profession'].strip()
    if p == 'C&N Specialist':
        continue
    if p + '.csv' in files:
        try:
            tf = pd.read_csv('../Data/Scraped_data/JobsChApi/' + p + '.csv')
            alternatives_names = list(tf['name_display'])
        except Exception as e:
            print(e)

    another_name = str(r['another_name']).replace('Der ', '') if len(str(r['another_name'])) > 0 else ''
    Synonyme = str(r['Synonyme']).split(', ') if len(str(r['Synonyme'])) > 0 else ''
    similar_titles = ast.literal_eval(r['Verwandte Berufe']) if isinstance(r['Verwandte Berufe'], str) else []
    Rubriken = ast.literal_eval(r['Rubriken']) if isinstance(r['Verwandte Berufe'], str) else []
    if len(Rubriken) > 0:
        print([p, another_name, alternatives_names, Synonyme, similar_titles, Rubriken])
        arr.append([p, another_name, alternatives_names, Synonyme, similar_titles, Rubriken])

    # c += 1
    # if c == 10:
    #     break

out = pd.DataFrame(arr, columns=['profession', 'another_name', 'alternatives_names', 'synonyme', 'similar_titles',
                                 'rubriken'])
out.to_csv('../Data_files/all_fields_merged.csv', index=False, encoding='utf-8')
