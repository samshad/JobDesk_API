import pandas as pd
from PreProcessing.clean_text import clean_text

df = pd.read_csv('../Data/VacData/top_50_data.csv')

arr = []
# Educations,ProfessinalExperiences,Skills,Languages,Documents,JobTitle,InternalRefCode
# InternalRefCode,JobTitle,Profexp,Edu,Skills
# df['Skills'] = df['Skills'].apply(lambda x: ast.literal_eval(x))

for i, r in df.iterrows():
    skills_list = list(set(str(r['Skills']).split()))
    skills = ''
    if len(skills_list) > 0:
        for t in skills_list:
            skills += ' ' + clean_text(t)
    clean_Profexp = clean_text(str(r['Profexp']))
    edu = str(r['Edu']).split()
    if len(edu) > 0:
        tmp = clean_text(' '.join(edu))
        clean_Edu = tmp if tmp != 'nan' else ''
    else:
        clean_Edu = ''
    arr.append([r['InternalRefCode'], r['JobTitle'], clean_Profexp, clean_Edu, skills])

out = pd.DataFrame(arr, columns=['InternalRefCode', 'JobTitle', 'Profexp', 'Edu', 'Skills'])
# out.dropna()
out.to_csv('../Data/VacData/cleaned_data.csv', index=False)
