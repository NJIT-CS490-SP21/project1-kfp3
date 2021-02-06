import os
import requests
from dotenv import load_dotenv,find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

load_dotenv(find_dotenv())


#This function is purely for retreiving the data. That's it. I hardcoded in 3 separate artist id's.
def find_albums():
    
    #These are my artist id's. 
    jack_johnson_uri = 'spotify:artist:3GBPw9NK25X1Wt2OUvOwY3'
    heilung_uri = 'spotify:artist:7sTKZr30LqC928DZ5P9mNQ'
    ville_uri = 'spotify:artist:6Kvpu1Xs687rTFj4qlGg4h'
    
    
    #This is setting up to randomly choose one of the artists.
    artists = [jack_johnson_uri,heilung_uri,ville_uri]
    num = random.randint(0,2)
    
    
    
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    #And here, the artist is randomly chosen and their data is returned to app.py
    results = spotify.artist_top_tracks(artists[num])
    return results
