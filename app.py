import os
from Flask import Flask, render_template
import requests
from dotenv import load_dotenv,find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

@app.route('/')
def display():
    find_albums()
    

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)