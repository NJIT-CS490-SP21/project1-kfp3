import os
import requests
from dotenv import load_dotenv,find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

load_dotenv(find_dotenv())

def find_albums():
    jack_johnson_uri = 'spotify:artist:3GBPw9NK25X1Wt2OUvOwY3'
    heilung_uri = 'spotify:artist:7sTKZr30LqC928DZ5P9mNQ'
    ville_uri = 'spotify:artist:6Kvpu1Xs687rTFj4qlGg4h'
    
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    
    results = spotify.artist_albums(jack_johnson_uri, album_type='album')
    albums = results['items']
    while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
    
    for album in albums:
    print(album['name'])