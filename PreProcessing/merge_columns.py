import pandas as pd
import ast


df = pd.read_csv('../Data_files/all_fields_merged.csv')

arr = []

for i, r in df.iterrows():
    text = r['profession']
    text += ' ' + r['another_name'] if isinstance(r['another_name'], str) else ''
    text += ' ' + ' '.join(ast.literal_eval(r['alternatives_names'])) if isinstance(r['alternatives_names'], str) else ''
    text += ' ' + ' '.join(ast.literal_eval(r['synonyme'])) if isinstance(r['synonyme'], str) else ''
    text += ' ' + ' '.join(ast.literal_eval(r['similar_titles'])) if isinstance(r['similar_titles'], str) else ''
    text = text.replace("nan", "")
    text = ' '.join(text.split())
    arr.append([text, r['rubriken']])

out = pd.DataFrame(arr, columns=['text', 'sectors'])
out.to_csv('../Data_files/dataset_sector.csv', index=False, encoding='utf-8')

