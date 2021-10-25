import pandas as pd
from collections import Counter


df = pd.read_csv('../Data/VacData/ini_dataset.csv')

arr = []
# Educations,ProfessinalExperiences,Skills,Languages,Documents,JobTitle,InternalRefCode
# InternalRefCode,JobTitle,Profexp,Edu,Skills
# df['Skills'] = df['Skills'].apply(lambda x: ast.literal_eval(x))

for i, r in df.iterrows():
    for w in r['text'].split():
        arr.append(w)

w_cnt = Counter(arr)
print(w_cnt)
