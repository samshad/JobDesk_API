import pandas as pd


df = pd.read_csv('../Data/Dataset/linkedin_proflies.csv')

arr = []
for i, r in df.iterrows():
    pre = r['occupation']
    post = r['occupation'].split(' at ')[0]
    # print(pre, "==>", post)
    arr.append([r['text'], r['summery'], post])

tf = pd.DataFrame(arr, columns=['text', 'summery', 'occupation'])
tf.to_csv('Data/Dataset/linkedin_proflies.csv', index=False)
