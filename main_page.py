import spotipy
import os
from flask import Flask, request

import pandas as pd
import boto3


def load_html():
    client_id = 'e6be6a0e60124f36ad99038de2f36e91'
    client_secret = '14116a664bd84048a0c7c3004edc9726'

    # Temporary placeholder until we actually get a website going
    # redirect_uri = 'http://127.0.0.1:5000/callback/'
    redirect_uri = 'https://initialflaskapp.herokuapp.com/callback/'

    # The permissions that our application will ask for
    scope = " ".join(['playlist-modify-public',"user-top-read","user-read-recently-played","playlist-read-private"])

    # Oauth object    
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

    # Force auth every time
    auth_url = sp_oauth.get_authorize_url()

    # client = boto3.client('s3')

    # path_user_profile = 's3://capstone-training-data/user_profile.tsv'
    # path_user_artists = 's3://capstone-training-data/user_artist.tsv'

    # cols_user_profile = ['user_id', 'gender', 'age', 'country', 'date']
    # cols_user_artist = ['user_id', 'artist_id', 'artist_name', 'plays']

    # print('Downloading user_profile')
    # user_profile = pd.read_csv(path_user_profile,
    #                       sep = '\t',
    #                       names = cols_user_profile)

    # print('Downloading user_artist')
    # user_artist = pd.read_csv(path_user_artists,
    #                      sep = '\t',
    #                      names = cols_user_artist)

    # user_profile.to_csv('user_profile.csv')
    # user_artist.to_csv('user_artist.csv')

     user_profile = pd.read_csv('user_profile.tsv',
                          sep = '\t',
                          names = cols_user_profile)

    user_artist = pd.read_csv('user_artist.tsv',
                         sep = '\t',
                         names = cols_user_artist)

   

  
    

    # ----------------------------------- Generate HTML -----------------------------------
    page_html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="A layout example that shows off a responsive product landing page.">
        <title>Landing Page &ndash; Layout Examples &ndash; Pure</title>
    </head>
    <body>

    <div class="header">
        <div class="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
            <a class="pure-menu-heading" href="">Your Site</a>

            <ul class="pure-menu-list">
                <li class="pure-menu-item pure-menu-selected"><a href="#" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="#" class="pure-menu-link">Tour</a></li>
                <li class="pure-menu-item"><a href="#" class="pure-menu-link">Sign Up</a></li>
            </ul>
        </div>
    </div>

    <div class="splash-container">
        <div class="splash">
            <h1 class="splash-head">All Capstone No Cap</h1>
            <p class="splash-subhead">
                Finding music that parents can listen to with their children
            </p>
            <p>
                <a href="{}" class="pure-button pure-button-primary">Get Started</a>
            </p>

            <p> Shape of df 1: {} </p>
            
            <p> Shape of df 2: {} </p>
        </div>
    </div>
    </body>
</html>
     """.format(auth_url, user_profile.head(), user_artist.head())

    return page_html
