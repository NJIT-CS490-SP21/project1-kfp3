I started the project on Friday, but I kept on having problems with git. I had to reinitialize git inside Project1, which I didn't understand at first,
and I didn't want empty directories on the related repo in Github, so I had to also learn to change and delete branches, pull before push, etc.

I continued on Saturday, wherein I actually began creating the code. I am not a graphic designer by any means, so I just wanted to create a very simple
html document that could display my favorite artists. I know that I can find artists using the api, searching by their name, but I figured since
the project allows me to just hardcode their id's in, I decided to go with that for simplicity's sake. 

It also turns out that not every song on Spotify actually has a preview_url, so don't expect one for every song.

I separated my functions between 3 different files named after their respective functionalities. For the Genius portion of the project, I decided to use a library I found online: https://pypi.org/project/lyricsgenius/

I was having an issue with CSS. I know that my CSS code is correct, but it doesn't update on my app. I tried hard refreshing the page, clearing the cache, and adding a code snippet recommended by David Kim. 
I just gave up after it didn't want to work.

At first, my heroku app wouldn't deploy because of an error with spotipy. I managed to resolve it by just using pip freeze rather than manually entering the data.