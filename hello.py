# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello World!"

@app.route('/min.json')
def mine():
        with open('min.json', 'r') as ctx:
                return ctx.read()
        return '{"error":"Couldn\'t open file for reading"}'

