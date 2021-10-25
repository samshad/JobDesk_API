import pandas as pd
import json


for id in range(6, 7):
    file = f'Data/VacData/S2/vacdata_{id}.json5'

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(len(data))

    arr = []
    cnt = 0
    for i in data:
        for p in i['Profiles']:
            skills = []
            for s in p['Skills']:
                skills.append(' '.join(s.split()).lower())
            ProfessinalExperiences = ''
            for pe in p['ProfessinalExperiences']:
                ProfessinalExperiences += pe.lower() + ' '
            ProfessinalExperiences = ' '.join(ProfessinalExperiences.split())
            # ProfessinalExperiences = get_clean(ProfessinalExperiences)
            if len(i['JobTitle']) > 0 and len(ProfessinalExperiences.split()) > 10:
                arr.append([ProfessinalExperiences, skills,
                            i['JobTitle'].lower(), i['InternalRefCode']])

    df = pd.DataFrame(arr, columns=['ProfessinalExperiences', 'Skills', 'JobTitle', 'InternalRefCode'])
    df.to_csv(f'Data/Dataset/jobtitle_profile{id}.csv', index=False)

# for i in data:
#     arr.append({'InternalRefCode': i['InternalRefCode'], 'JobTitle': i['JobTitle'],
#                 'JobAdText': get_clean(i['JobAdText']), 'OtherJobTitles': i['OtherJobTitles']})
#
# print(arr)
#
# with open('Data/Dataset/sample.json5', 'w', encoding='utf-8') as f:
#     json.dump(arr, f, ensure_ascii=False, indent=4)
#
# df = pd.json_normalize(arr)
# df.to_csv('Data/Dataset/sample.csv', index=False)

# for i in data:
#     arr.append([i['InternalRefCode'], i['JobTitle'], i['JobAdText'], i['OtherJobTitles']])

# df = pd.DataFrame(arr, columns=['InternalRefCode', 'JobTitle', 'JobAdText', 'OtherJobTitles'])
# print(df.head().to_string(index=False))
# print(df['JobTitle'].value_counts())
# df.to_csv('Data/Dataset/jobtitle_jobtext.csv', index=False)

