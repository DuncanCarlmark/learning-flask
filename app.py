# Web and Server
from flask import Flask, request
import requests
from io import StringIO

# Downloading Data
import boto3
import pandas as pd

# Page imports
import main_page, callback_page


app = Flask(__name__)

@app.route('/')
def idex():

    return main_page.load_html()

@app.route('/callback/')
def callback():
    code = request.args.get('code')
    print("WE GOT DA CODE")
    print(code)

    sp_auth = ()
    return callback_page.load_html()


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)