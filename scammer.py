from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback


app = Flask(__name__, static_folder='static')

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/test')
def test():
    return render_template('test.html')


