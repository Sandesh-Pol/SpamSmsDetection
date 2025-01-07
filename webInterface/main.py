# spam_classifier.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
import re
import sklearn
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# Cell 2
import os
file_path = os.path.join(r'C:\Users\Admin\Desktop\Project\SMS-SPAM\SPAM-SMS-Prediction-master\SpamSmsDetection', 'Spam SMS Collection')
sms = pd.read_csv(file_path, sep='\t', names=['label', 'message'])
sms.drop_duplicates(inplace=True)
sms.reset_index(drop=True, inplace=True)

corpus = []
ps = PorterStemmer()

for i in range(0, sms.shape[0]):
    message = re.sub(pattern='[^a-zA-Z]', repl=' ', string=sms.message[i])
    message = message.lower()
    words = message.split()
    words = [word for word in words if word not in set(stopwords.words('english'))]
    words = [ps.stem(word) for word in words]
    message = ' '.join(words)
    corpus.append(message)

# Cell 3
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()

y = pd.get_dummies(sms['label'])
y = y.iloc[:, 1].values

# Cell 4
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

classifier = MultinomialNB(alpha=0.1)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

acc_s = accuracy_score(y_test, y_pred) * 100
print("Accuracy Score {} %".format(round(acc_s, 2)))

# Cell 5
def predict_spam(sample_message):
    sample_message = re.sub(pattern='[^a-zA-Z]', repl=' ', string=sample_message)
    sample_message = sample_message.lower()
    sample_message_words = sample_message.split()
    sample_message_words = [word for word in sample_message_words if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    final_message = [ps.stem(word) for word in sample_message_words]
    final_message = ' '.join(final_message)
    temp = cv.transform([final_message]).toarray()
    return classifier.predict(temp)

# Cell 6
result = ['this is a SPAM!', 'Ohhh, this is a normal message.']



