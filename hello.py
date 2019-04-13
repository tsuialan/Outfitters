#!/usr/bin/python
from flask import Flask, render_template, redirect, request
import os
import scripts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/script/')
def index2():
    scripts.genResponse()
    scripts.genKeywords()
    url = scripts.genUrl()
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run(debug=True)