from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback

import string
import pandas as pd
import numpy as np 

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

nltk.download('stopwords')

df = pd.read_csv('spam_ham_dataset.csv')
df['text'] = df['text'].apply(lambda x: x.replace('\r\n', ' '))
    
stemmer = PorterStemmer()
corpus = []

stopwords_set = set(stopwords.words('english'))

for i in range(len(df)):
    text = df['text'].iloc[i].lower()
    splitText = text.translate(str.maketrans('','', string.punctuation)).split()
    stemList = []
    for word in splitText:
        stem = stemmer.stem(word)
        if stem not in stopwords_set:
            stemList.append(stem)

    corpus.append(' '.join(stemList))
    

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus).toarray()
y = df.label_num


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)
clf = RandomForestClassifier(n_jobs=-1)
clf.fit(x_train, y_train)

def detectScam(inputText):
    text = inputText.lower().translate(str.maketrans('', '', string.punctuation)).split()
    text = [stemmer.stem(word) for word in text if word not in stopwords_set]
    text = ' '.join(text)

    email = [text]
    x_email = vectorizer.transform(email)
    return clf.predict(x_email)

app = Flask(__name__, static_folder='static')

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/test')
def test():
    try:
        return render_template('test.html')
        

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})

@app.route('/reemail', methods=['POST'])
def reemail():
        
        data = request.get_json()
        text = data.get('text')
        print(text)
        scam = False
        phish = detectScam(text)
        print(phish)
        if phish == 1:
            phish = 'Phishing Detected.'
        else:
            phish = 'This message appears to be safe.'

        print(phish)
            
        return render_template('test.html',phish=phish)
        