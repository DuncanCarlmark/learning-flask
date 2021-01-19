from flask import Flask, request
import pandas as pd
import requests
from io import StringIO

# Page imports
import main_page, callback_page


app = Flask(__name__)

@app.route('/')
def idex():

    orig_url = 'https://drive.google.com/file/d/1N4ZFdyvULQ0gQDxGsvMFURdiaV94y1F_/view?usp=sharing'

    columns = []
    file_id = orig_url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
    url = requests.get(dwn_url).text
    csv_raw = StringIO(url)
    dfs = pd.read_csv(csv_raw, sep = '\t')
    print("SHIT GOT LOADED POGGERS")


    return main_page.load_html()

@app.route('/callback/')
def callback():
    code = request.args.get('code')
    print("WE GOT DA CODE")
    print(code)

    sp_auth = ()
    return callback_page.load_html()


if __name__ == '__main__':
    app.run(debug=True)