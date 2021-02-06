import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv,find_dotenv
from spotify import *
import random

#app = Flask(__name__)

#@app.route('/')
def display():
    #Fetching artist's data.
    lst = find_albums()
    
    #Creating random number so the same song won't always be shown.
    num=random.randint(0,9)
    
    #Pass data to index.html
    track = lst['tracks'][num]
    name='track    : ' + track['name']
    artist_name = lst['tracks'][0]['album']['artists'][0]['name']
    if track['preview_url'] is not None:
        url= 'audio    : ' + track['preview_url']
    else:
        url='There is no preview url for this specific song.'
    album_cover='cover art: ' + track['album']['images'][0]['url']
    print()
    #return render_template(
     #   "index.html",
      #  artists=lst,
    #)
if __name__ == '__main__':
    display()
#app.run(
 #   port=int(os.getenv('PORT', 8080)),
  #  host=os.getenv('IP', '0.0.0.0')
#)