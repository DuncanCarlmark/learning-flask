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
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="A layout example that shows off a responsive product landing page.">
        <title>Landing Page &ndash; Layout Examples &ndash; Pure</title>
        <link rel="stylesheet" type="text/css" href="\styling\pure_min.css">
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
                <a href="http://purecss.io" class="pure-button pure-button-primary">Get Started</a>
            </p>
        </div>
    </div>
    </body>
</html>
     """.format(auth_url)

    return page_html
