import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv,find_dotenv
from spotify import *
from genius import *
import random

app = Flask(__name__)
app.debug=True

@app.route('/')
def display():
    #Fetching artist's data.
    lst = find_albums()
    
    #Creating random number so the same song won't always be shown.
    num=random.randint(0,9)
    
    #Pass data to index.html by choosing individual track.
    track = lst['tracks'][num]
    
    #Track name.
    name='track    : ' + track['name']
    
    lyrics=fetchLyrics(name)
    
    #Artist's name
    artist_name = lst['tracks'][0]['album']['artists'][0]['name']
    #Check if song has preview url. Otherwise print something else.
    if track['preview_url'] is not None:
        url=track['preview_url']
    else:
        url='There is no preview url for this specific song.'
        
    #Album cover
    album_cover=track['album']['images'][0]['url']
    #This is where the data gets passed.
    return render_template(
        "index.html",
        artist=artist_name,
        track_name=name,
        cover=album_cover,
        track_preview=url
    )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)