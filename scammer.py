from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback
import pandas, nltk


app = Flask(__name__, static_folder='static')

def detectScam(text):
     countFlags = 0
     badwords= ['vulnerability', 'click here', 'click here to', 'security reasons', 'urgent', 'postal', 'alert', 'immediate']
     
     for word in badwords:
        if text.contains(word):
            countFlags = countFlags + 1


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
        print('hello')
        data = request.get_json()
        text = data.get('text')
        print(text)
        scam = False
        flags = ['']

        print(text)
            
        return render_template('test.html', flags = flags, scam = scam)
        

