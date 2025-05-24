import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/test')
def hello_world():
    return 'test'