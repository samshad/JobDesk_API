import pandas as pd
from collections import Counter


df = pd.read_csv('../Data/VacData/merged_all_unique.csv')

arr = []
# Educations,ProfessinalExperiences,Skills,Languages,Documents,JobTitle,InternalRefCode
# InternalRefCode,JobTitle,Profexp,Edu,Skills
# df['Skills'] = df['Skills'].apply(lambda x: ast.literal_eval(x))

xx = list(df['JobTitle'])
yy = Counter(xx)
print(yy)

# for i, r in df.iterrows():
#     if yy[r['JobTitle']] >= 50:
#         arr.append([r['InternalRefCode'], r['JobTitle'], r['Profexp'], r['Edu'], r['Skills']])

# out = pd.DataFrame(arr, columns=['InternalRefCode', 'JobTitle', 'Profexp', 'Edu', 'Skills'])
# out.dropna()
# out.to_csv('../Data/VacData/top_50_data.csv', index=False)
