import pandas as pd


jdf = pd.read_csv('Data/Dataset/OLD/Jobtitle_jobtext.csv')
odf = pd.read_csv('Data/train_occupations_de.csv')

jobtitles = list(set(list(jdf['JobTitle'])))
occupations = list(set(list(odf['preferredLabel'])))

print(len(jobtitles))
count = 0
for o in occupations:
    if o in jobtitles:
        count += 1
print(count)

