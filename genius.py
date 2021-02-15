import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv,find_dotenv
import lyricsgenius

load_dotenv(find_dotenv())

def fetchLyrics(artistName,songName):
    token=os.getenv('GENIUS_CLIENT_ACCESS_TOKEN')
    genius = lyricsgenius.Genius(token)
    artist = genius.search_artist(artistName, max_songs=3, sort="title", include_features=False)
    song = genius.search_song(songName, artist.name)
    if song is None:
        return "No lyrics could be found for this song"
    else:
        return song.url
