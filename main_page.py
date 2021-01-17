import spotipy
import os

def load_html():
    client_id = 'f78a4f4cfe9c40ea8fe346b0576e98ea'
    client_secret = 'c26db2d4c1fb42d79dc99945b2360ab4'

    # Temporary placeholder until we actually get a website going
    redirect_uri = 'https://google.com/'

    # The permissions that our application will ask for
    scope = " ".join(['playlist-modify-public',"user-top-read","user-read-recently-played","playlist-read-private"])

    # Oauth object    
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

    # Force auth every time
    auth_url = sp_oauth.get_authorize_url()
    

    page_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1> HEHE TIME FOR PLAYLIST RECOMMENDATION </h1>

        <a href="{}"> Please click on this link to make a playlist</a>
        
    </body>
    </html>
     """.format(auth_url)

    return page_html
