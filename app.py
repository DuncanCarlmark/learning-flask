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

    # ----------------------------------- Download Data from S3 -----------------------------------

    client = boto3.client('s3')

    path_user_profile = 's3://capstone-training-data/user_profile.tsv'
    path_user_artists = 's3://capstone-training-data/user_artist.tsv'

    cols_user_profile = ['user_id', 'gender', 'age', 'country', 'date']
    cols_user_artist = ['user_id', 'artist_id', 'artist_name', 'plays']

    print('Downloading user_profile')
    user_profile = pd.read_csv(path_user_profile,
                          sep = '\t',
                          names = cols_user_profile)

    print('Downloading user_artist')
    user_artist = pd.read_csv(path_user_artists,
                         sep = '\t',
                         names = cols_user_artist)

    user_profile.to_csv('user_profile.csv')
    user_artist.to_csv('user_artist.csv')


    app.run(debug=True)