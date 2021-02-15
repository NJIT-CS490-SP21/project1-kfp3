import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv,find_dotenv
import lyricsgenius

load_dotenv(find_dotenv())

def fetchLyrics(artistName,songName):
    
    
    token=os.getenv('GENIUS_CLIENT_ACCESS_TOKEN')
    
    #An online library that made my life easier.
    genius = lyricsgenius.Genius(token)
    
    #Fetch artist info
    artist = genius.search_artist(artistName, max_songs=3, sort="title", include_features=False)
    
    #Fetch song info
    song = genius.search_song(songName, artist.name)
    
    #In case there was an error
    if song is None:
        return "No lyrics could be found for this song"
    else:
        return song.url
