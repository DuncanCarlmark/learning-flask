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
  
    

    # ----------------------------------- Generate HTML -----------------------------------
    page_html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Website for DSC180b capstone project in recommender systems">
        <title>Capstone Recommender</title>
    </head>
    <body>

    <div>
        <div>
            <h1>All Capstone No Cap</h1>
            <p>
                Finding music that parents can listen to with their children
            </p>
            <p>
                <a href="{}" >Get Started</a>
            </p>     
        </div>
    </div>
    </body>
    </html>
     """.format(auth_url)

    return page_html
