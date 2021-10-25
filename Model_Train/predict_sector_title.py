import pandas as pd
import pickle


def get_sector(x):
    with open('Predict_Sectors_Models/sector_tfidf.pkl', 'rb') as pickle_file:
        tfidf = pickle.load(pickle_file)

    with open('Predict_Sectors_Models/sector_model.pkl', 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    with open('Predict_Sectors_Models/sector_multilabel.pkl', 'rb') as pickle_file:
        multilabel = pickle.load(pickle_file)

    xt = tfidf.transform([x])
    pred = model.predict(xt)
    sectors = multilabel.inverse_transform(pred)
    # print(x, " ==> ", sectors)
    return sectors


if __name__ == '__main__':
    x = get_sector("python developer")
    print(x)
