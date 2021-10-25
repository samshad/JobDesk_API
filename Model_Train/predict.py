import pandas as pd
import pickle


# df = pd.read_csv('../Data/sample.csv')
# # print(df.head().to_string(index=False))
# x = df['sample'][0]


def get_prediction(x):
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

    # df = pd.read_csv('../Data/train_occupations.csv')
    # arr = []
    # for tag in tags[0]:
    #     tf = df[df['PreferredLabel_num'] == int(tag)]
    #     print(tf['PreferredLabel'])
    #     arr.append(tag + '-' + str(list(tf['ISCO'])[0]))


if __name__ == '__main__':
    df = pd.read_csv('../Data_files/VacData/all_professions.csv')

    c = 0
    arr = []

    for i, r in df.iterrows():
        x = r['Professions'].strip()
        given_sector = r['Sector/Industry']
        predicted_sector = get_prediction(x)
        arr.append([x, given_sector, predicted_sector])

    out = pd.DataFrame(arr, columns=['profession', 'given_sector', 'predicted_sector'])
    out.to_csv('../Data_files/predicted_sectors.csv', index=False, encoding='utf-8')

    # x = df['Professions'].iloc[10]
    # print(x)
    # get_prediction(x)
    # for i, r in df.iterrows():
    #     get_prediction(r['text'])
