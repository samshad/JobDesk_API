from fastapi import FastAPI
from post_data import PostData
from geo_location import get_location
from gpe import Get_LOC
import pickle
import pandas as pd
from langdetect import detect


app = FastAPI()
print("importing tfidf...", flush=True)
with open('/home/JobDesk_API/Model/svc_tfidf_de.pkl', 'rb') as pickle_file:
    tfidf = pickle.load(pickle_file)
print("importing tfidf done...", flush=True)

print("importing svc model...", flush=True)
with open('/home/JobDesk_API/Model/svc_model_de.pkl', 'rb') as pickle_file:
    model = pickle.load(pickle_file)
print("importing svc model done...", flush=True)

print("importing multilabel...", flush=True)
with open('/home/JobDesk_API/Model/multilabel_de.pkl', 'rb') as pickle_file:
    multilabel = pickle.load(pickle_file)
print("importing multilabel done...", flush=True)

df = pd.read_csv('/home/JobDesk_API/Data/train_occupations_de.csv')


@app.get('/')
def index():
    return {'message': 'API up and running'}


@app.post('/predict')
def predict_label(data: PostData):
    data = data.dict()

    print("in => \n", data, flush=True)

    # extracting payload
    doc = data['data']
    uid = data['uid']
    lc = data['lc']

    if len(doc) < 1:
        return {
            "error": "empty document."
        }

    lang = detect(doc)
    print("vectorize and predict...", flush=True)
    xt = tfidf.transform([doc])
    pred = model.predict(xt)
    print("vectorize and predict done...", flush=True)
    tags = multilabel.inverse_transform(pred)

    arr = []
    for tag in tags[0]:
        tf = df[df['preferredLabel_num'] == int(tag)]
        arr.append(tag + '-' + str(list(tf['iscoGroup'])[0]))

    # getting LOC from spacy
    LOC = Get_LOC(doc)

    if data['geoLat'] is not None and data['geoLong'] is not None:
        address = get_location(data['geoLat'], data['geoLong'])
        ret = {
            'uid': uid,
            'tags': arr,
            'lang': lang,
            'Locations': LOC,
            'GeoAddress': address
        }

    else:
        ret = {
            'uid': uid,
            'tags': arr,
            'lang': lang,
            'Locations': LOC
        }

    print("out => \n", ret, flush=True)

    return ret


"""if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)"""

# uvicorn app:app --reload

