# -*- coding: utf-8 -*-
"""Train_ini_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQTrVDwvHzkf1TlINiXZuJb7g-IpobXs
"""

from google.colab import drive
drive.mount('/gdrive')

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

from sklearn.multiclass import OneVsRestClassifier

df = pd.read_csv('/gdrive/MyDrive/Dataset_Jobdesk/dataset_sector.csv')

df = pd.read_csv('/gdrive/MyDrive/Dataset_Jobdesk/ini_dataset.csv')

df.head()

df['sectors'].iloc[0]

import ast

ast.literal_eval(df['sectors'].iloc[0])

df['sectors'] = df['sectors'].apply(lambda x: ast.literal_eval(x))
# df['title'] = df['title'].apply(lambda x: [str(x)])

multilabel = MultiLabelBinarizer()

y = multilabel.fit_transform(df['sectors'])

y

multilabel.classes_

# tfidf = TfidfVectorizer(analyzer='word', max_features=10000, ngram_range=(1,3))
tfidf = TfidfVectorizer(analyzer='word')
X = tfidf.fit_transform(df['text'])

X.shape, y.shape

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

X_train = X
y_train = y

sgd = SGDClassifier()
lr = LogisticRegression(solver='lbfgs')
svc = LinearSVC()
nb = MultinomialNB()

def j_score(y_true, y_pred):
    jaccard = np.minimum(y_true, y_pred).sum(axis = 1)/np.maximum(y_true, y_pred).sum(axis = 1)
    return jaccard.mean()*100


def print_score(y_pred, clf):
    print("Clf: ", clf.__class__.__name__)
    print('Jacard score: {}'.format(j_score(y_test, y_pred)))
    print('----')

for classifier in [sgd, lr, svc, nb]:
    clf = OneVsRestClassifier(classifier)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print_score(y_pred, classifier)

for classifier in [sgd]:
    clf = OneVsRestClassifier(classifier)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print_score(y_pred, classifier)

x = [' Business Analyst/Requirement Engineer, Data Scientist']

x = ["lagermitarbeit auslager transport unterst uuml tzung betriebssystem axapta einwandfrei lager termingerecht fehlerlos bearbeit kundenauftr auml ge materialbereitstell verschied allgemein logistikaufgab betriebsmitarbeit temorar lagermitarbeit einlag neu eingebucht wareneingangswar kleinteilelag artikel kundenr uuml ckgab sowi nachschub vorrat reservelag autostor einlag intern materialtransport sicherstell ausf uuml hren nachschub reserveartikel uuml autostor bereitstell allgemein aufgab logist"]

x = ["servicetechn servic reparaturarberit entkalkungsanlag auml ndig telefon terminorganisation technisch berat kundschaft chefmonteur abwickl spezial problemauftr auml gen terminier auftr auml ge technisch unterst uuml tzung montag standortausbildn kundenberat massaufnahm mitwirk pikett eskalation stellvertret leit stor servic offert bestellwes fehlermeld erstell servicetechn region zentralschweiz montag wartungsarbeit halb vollautomat kaffeemaschin kund einsatz pikettdien gem auml ss einsatzplan fahrradmechan allround temporar anstell ubergangslos sachbearbeit disposition ubergangslos servicetechn neumontag find beheb st ouml rung divers reparaturarbeit erstell offert uuml reparatur automonteur lehrlingsausbild reparatur unterhaltsarbeit person lieferwag motorr auml dern carrosseriearbeit allgemein administrativ aufgab ndash handelsschul vollzeit ndash automonteur carrosseriespengl tempor auml re anstell automonteur auml hrig lehr automonteur efz jahrig zusatzlehr carrosseriespengl efz automonteur allround"]

xt = tfidf.transform(x)

xt

clf.predict(xt)

multilabel.inverse_transform(clf.predict(xt))

import pickle

with open('/gdrive/MyDrive/Dataset_Jobdesk/SGD_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

# with open('/gdrive/MyDrive/Dataset_Jobdesk/SGD_tfidf.pkl', 'wb') as f:
#     pickle.dump(tfidf, f)

# with open('/gdrive/MyDrive/Dataset_Jobdesk/multilabel.pkl', 'wb') as f:
#     pickle.dump(multilabel, f)