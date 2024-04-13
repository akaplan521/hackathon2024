from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback


# Defines flask app and specifys where to look for html and static resources
app = Flask(__name__, template_folder='/', static_folder='/static')

@app.route('/')
def start():
    return 0



