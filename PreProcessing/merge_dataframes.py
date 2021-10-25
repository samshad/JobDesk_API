import pandas as pd
from tqdm import tqdm


arr = []

# Educations,ProfessinalExperiences,Skills,Languages,Documents,JobTitle,InternalRefCode

# for id in tqdm(range(1, 9)):
#     path = f'../Data/VacData/{id}.csv'
#     df = pd.read_csv(path)
#     for i, r in df.iterrows():
#         arr.append([
#             r['CID'], r['Professions'], r['Sector/Industry'], r['ProfExp'], r['Edu'], r['Skills']
#         ])
#
# out = pd.DataFrame(arr, columns=['CID', 'Professions', 'Sector/Industry', 'ProfExp', 'Edu', 'Skills'])
# out.to_csv('../Data/VacData/merged_all.csv', index=False)

df1 = pd.read_csv('../Data_files/dataset_sector.csv')
df2 = pd.read_csv('../Data_files/generalized_sectors.csv')

for i, r in df1.iterrows():
    arr.append([r['texts'], r['sectors']])

for i, r in df2.iterrows():
    arr.append([r['texts'], r['sectors']])

out = pd.DataFrame(arr, columns=['texts', 'sectors'])
out.to_csv('../Data_files/merged_dataset_sectors.csv', index=False)
