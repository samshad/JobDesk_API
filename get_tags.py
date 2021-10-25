import pickle
import pandas as pd


print("importing tfidf...", flush=True)
with open('Model/svc_tfidf_de.pkl', 'rb') as pickle_file:
    tfidf = pickle.load(pickle_file)
print("importing tfidf done...", flush=True)

print("importing svc model...", flush=True)
with open('Model/svc_model_de.pkl', 'rb') as pickle_file:
    model = pickle.load(pickle_file)
print("importing svc model done...", flush=True)

print("importing multilabel...", flush=True)
with open('Model/multilabel_de.pkl', 'rb') as pickle_file:
    multilabel = pickle.load(pickle_file)
print("importing multilabel done...", flush=True)

df = pd.read_csv('Data/train_occupations_de.csv')


def get_tags(doc):
    print("vectorize and predict...", flush=True)
    xt = tfidf.transform([doc])
    pred = model.predict(xt)
    print("vectorize and predict done...", flush=True)
    tags = multilabel.inverse_transform(pred)

    arr = []
    for tag in tags[0]:
        tf = df[df['preferredLabel_num'] == int(tag)]
        arr.append(tag + '-' + str(list(tf['iscoGroup'])[0]))

    return arr
