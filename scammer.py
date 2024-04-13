from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback


app = Flask(__name__, static_folder='static')

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/test', methods=['POST','GET'])
def test():
    try:
        if request.method == 'POST':
            print('hello')
            data = request.get_json()
            text = data.get('searchQuery')
            scam = False
            flags = ['']

            print(text)
            
            return render_template('test.html', data = flags, scam = scam)
        

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})



