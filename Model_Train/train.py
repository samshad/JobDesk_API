import pandas as pd
import numpy as np
import pickle
import ast

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import time


def j_score(y_true, y_pred):
    jaccard = np.minimum(y_true, y_pred).sum(axis=1)/np.maximum(y_true, y_pred).sum(axis=1)
    return jaccard.mean()*100


def print_score(y_pred, clf):
    print("Clf: ", clf.__class__.__name__)
    print('Jacard score: {}'.format(j_score(y_test, y_pred)))
    print('----')


start_time = time.time()
df = pd.read_csv('../Data/Dataset/ini_dataset2.csv')
# print(df.head().to_string(index=False))

# df['title'] = df['title'].apply(lambda x: ast.literal_eval(x))
df['title_num'] = df['title_num'].apply(lambda x: [str(x)])

multilabel = MultiLabelBinarizer()
y = multilabel.fit_transform(df['title_num'])
print(multilabel.classes_)

tfidf = TfidfVectorizer(analyzer='word', max_features=50000, ngram_range=(1, 3))
X = tfidf.fit_transform(df['text'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

svc = LinearSVC()
# lr = LogisticRegression(solver='lbfgs')

# X_train = X
# y_train = y

# for classifier in [LinearSVC(C=1.5, penalty='l1', dual=False)]:
#     clf = OneVsRestClassifier(classifier)
#     clf.fit(X_train, y_train)

print("Fitting data started!")
clf = OneVsRestClassifier(svc)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print_score(y_pred, svc)

# print(accuracy_score(y_train, clf.best_estimator_.predict(X_train)))
# print(accuracy_score(y_test, clf.best_estimator_.predict(X_test)))

with open('svc_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('svc_tfidf.pkl', 'wb') as f:
    pickle.dump(tfidf, f)

with open('multilabel.pkl', 'wb') as f:
    pickle.dump(multilabel, f)

print("--- %s minutes ---" % ((time.time() - start_time) / 60))
