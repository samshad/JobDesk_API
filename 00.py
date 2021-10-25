import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
from collections import Counter
import re
import ast


# df = pd.read_csv('Data/ResumeDataSet_1.csv')
#
# print(df['category'].value_counts())
# tf = df[df['category'] == 'Java Developer']
# print(tf.head())
#
# x = list(tf['resume'])[0]
# print(prediction(x))
#
# df = pd.read_csv('Data/occupations_de.csv')
# le = LabelEncoder()
#
# df['preferredLabel_num'] = le.fit_transform(df['preferredLabel'])
#
# df.to_csv('train_occupations_de.csv', index=False)
#
# with open('SVC/Model/label_encoder_de.pkl', 'wb') as f:
#     pickle.dump(le, f)

# data = dict()
# data['a'] = 1
# data['b'] = 2
# print(data)
#
# if 'a' in data:
#     print('a paisi')
# if 'a' in data and 'b' in data:
#     print('2 paisi')
#
# if 'c' in data:
#     print('hoyta')

# df = pd.read_csv('Data/ResumeDataSet_1.csv')
#
# cnt = 0
#
# for i, r in df.iterrows():
#     if cnt == 17:
#         t = ' '.join(r['resume'].split())
#         print(t)
#         break
#     cnt += 1

# f = open("Data/sample_text.txt", "r")
# txt = f.read()
#
# df = pd.DataFrame([txt], columns=['text'])
# # df.to_csv('Data/sample_test.csv', index=False)
# print(df)

# df = pd.read_csv('Data/Dataset/ini_dataset.csv')
# df = pd.read_csv('Data/Dataset/dataset_counted.csv')
# df = pd.read_csv('Data/Dataset/linkedin_proflies.csv')
# print(df['occupation'].value_counts())
# # x = list(set(list(df['title'])))
# xx = list(df['occupation'])
# print(len(xx))
# # print("unique jobtitles: ", len(x))
# yy = Counter(xx)
#
# tf = pd.DataFrame.from_records(yy.most_common(), columns=['occupation', 'count'])
# print(df.head())
# tf.to_csv('Data/Dataset/occupation_linkedin.csv', index=False)

# arr = []
#
# for i, r in df.iterrows():
#     if yy[r['title']] >= 20:
#         arr.append([r['text'], r['title']])
#
# tf = pd.DataFrame(arr, columns=['text', 'title'])
# tf.to_csv('Data/Dataset/dataset_counted.csv', index=False)

# df = pd.read_csv('Data_files/merged_dataset_sectors.csv')
# print(df['sectors'].value_counts())
# x = list(set(list(df['InternalRefCode'])))
# xx = list(df['InternalRefCode'])
# yy = Counter(xx)
# print(yy)
# print(len(xx), len(x))

# x = list(set(list(df['JobTitle'])))
# xx = list(df['JobTitle'])
# yy = Counter(xx)
# print(yy)
# print(len(xx), len(x))

# st = 'abraxas 6102: System Administrator'
# st = 'abraxas: System Administrator'
# print(re.split(r'\d+: ', st)[1])

# arr = ['Administration/Sekretariat/Verwaltung', 'Banken/Versicherungen',
#        'Beratung/Recht', 'Chemie/Pharma', 'Diverse',
#        'Finanz- und Rechnungswesen/Controlling',
#        'Gastronomie/Hotellerie/Tourismus',
#        'Geschäftsführung / Unternehmensleitung',
#        'Gesundheitswesen/Medizin', 'Industrie/Ingenieurwesen/Technik',
#        'Informatik/Telekommunikation', 'Marketing',
#        'Non-Profit/Soziales/Bildungswesen', 'Others',
#        'Personalmanagement', 'Verkauf/Kundenberatung']
#
# print(arr)

df = pd.read_csv('Data_files/merged_dataset_sectors.csv')
print(df['sectors'].value_counts())
x = []
for i, r in df.iterrows():
    for l in ast.literal_eval(r['sectors']):
        x.append(l)

print(len(list(set(x))))
