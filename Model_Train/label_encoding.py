import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv('../Data/Dataset/dataset_counted.csv')

le = LabelEncoder()
df['title_num'] = le.fit_transform(df['title'])

df.to_csv('../Data/Dataset/ini_dataset2.csv', index=False)

with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)
# le.inverse_transform(prediction)
