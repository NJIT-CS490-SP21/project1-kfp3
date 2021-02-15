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
    the_high_kings_uri = 'spotify:artist:6wXjctGBzxkT0ghwfQ8FC0'
    nas_uri = 'spotify:artist:20qISvAhX20dpIbOOzGK3q'
    
    
    #This is setting up to randomly choose one of the artists.
    artists = [jack_johnson_uri,the_high_kings_uri,nas_uri]
    num = random.randint(0,2)
    
    
    
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    #And here, the artist is randomly chosen and their data is returned to app.py
    results = spotify.artist_top_tracks(artists[num])
    return results
