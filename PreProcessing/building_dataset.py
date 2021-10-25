import pandas as pd

df = pd.read_csv('../Data/VacData/cleaned_data.csv')

arr = []
# Educations,ProfessinalExperiences,Skills,Languages,Documents,JobTitle,InternalRefCode
# InternalRefCode,JobTitle,Profexp,Edu,Skills
# df['Skills'] = df['Skills'].apply(lambda x: ast.literal_eval(x))

for i, r in df.iterrows():
    skills = list(set(str(r['Skills']).split()))
    text = ' '.join(skills) if len(skills) > 0 else ''
    text += ' ' + str(r['Edu']) if len(str(r['Edu'])) > 0 else ''
    text += ' ' + str(r['Profexp'])
    text = text.replace("nan", "")
    text = ' '.join(text.split())
    if len(text) >= 10:
        arr.append([text, r['JobTitle']])

out = pd.DataFrame(arr, columns=['text', 'title'])
out.to_csv('../Data/VacData/ini_dataset.csv', index=False)
