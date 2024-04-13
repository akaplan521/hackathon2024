from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback


app = Flask(__name__, static_folder='static')

@app.route('/')
def start():
    return render_template('index.html')

#@app.route('/info')
#def info():
#    return 0

#@app.route('/test')
#def test():
#    return 0


