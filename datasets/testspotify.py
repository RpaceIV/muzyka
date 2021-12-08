from __future__ import print_function
# import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from pprint import pprint
# import pprint
from collections import namedtuple

import json
import time
import sys
import pandas as pd
import time

# SubGenre = namedtuple('SubGenre', 'name,prior_prob,song_amount')
# SongInfo = namedtuple('SongInfo', 'song,artist,album,genre,subgenre,prior_prob,q1,q2,q3,q4,q5')

class SubGenre:
    def __init__(self,name,prior_prob,song_amount,parent_genre):
        self.parent_genre = parent_genre
        self.name = name
        self.prior_prob = prior_prob
        self.song_amount = song_amount

class Song:
    def __init__(self,genre,subgenre,prior_prob):
        self.genre = genre
        self.subgenre = subgenre
        self.prior_prob = prior_prob

        self.name = ''
        self.artist = ''
        self.album = ''
        
        self.questions = [] #list of questions

        self.trackid = 0
        self.popularity = 0
        self.metadata = dict()

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def answerquestion(self, song):
    '''Q1'''
    if song.metadata['popularity'] > 70:
        song.questions[0] = 'a' #yes
    else:
        song.questions[0] = 'b' #no

    '''Q2'''
    if song.genre == 'World':
        song.questions[1] = 'a' #yes
    else:
        song.questions[1] = 'b' #no

    '''Q3'''
    if song.genre == 'electronic':
        song.questions[2] = 'a'
    elif song.genre == 'rap':
        song.questions[2] = 'b'
    elif song.genre == 'rock':
        song.questions[2] = 'c'
    elif song.genre == 'jazz':
        song.questions[2] = 'd'
    else:
        song.questions[2] = 'e' # Classical

    '''Q4'''
    if song.metadata['instrumentalness'] > 0.5:
        song.questions[3] = 'a' #beats
    else:
        song.questions[3] = 'b' #vocals

    # song.metadata['danceability'] > 0.5 and song.mmetadata['energy'] > 0.5 and song.mmetadata['loudness'] > 0.5 and song.mmetadata['valence'] > 0.9:
    '''Q5'''
    if song.metadata['danceability'] > 0.6 and song.mmetadata['energy'] > 0.5 and song.mmetadata['valence'] > 0.9:
        song.questions[4] = 'a' #happy
    elif song.metadata['danceability'] < 0.1 and song.mmetadata['energy'] < 0.1 and song.mmetadata['valence'] < 0.3:
        song.questions[4] = 'b' #sad
    elif song.mmetadata['energy'] > 0.7 and song.mmetadata['loudness'] > 0.6 and song.mmetadata['valence'] < 0.3:
        song.questions[4] = 'c' #angry
    elif song.metadata['danceability'] > 0.7 and song.mmetadata['energy'] > 0.8 and song.mmetadata['loudness'] > 0.6 and song.mmetadata['valence'] > 0.9:
        song.questions[4] = 'd' #hyped
    elif song.metadata['danceability'] > 0.5 and song.mmetadata['energy'] > 0.5 and song.mmetadata['loudness'] > 0.5 and song.mmetadata['valence'] > 0.5:
        song.questions[4] = 'e' #relaxed
    elif song.metadata['danceability'] > 1.0 and song.mmetadata['energy'] > 1.0 and song.mmetadata['loudness'] > 1.0 and song.mmetadata['valence'] > 1.0:
        song.questions[4] = 'f' #sensual
    
    return song

def main(search_str, subg, dfTwo, subgenre, block):
    type_str = 'playlist'
    market_str = 'US'
    limit_int = 50
    offs = 0
    print(block)

    '''searches for the playlist'''
    search_result = sp.search(search_str, limit_int,
                              offs, type_str, market_str)

    '''Selects the playlist'''
    if len(search_result['playlists']['items'][0]['name']) > len(search_str) and block == 1:
        for playnum in range(limit_int-1):
            if search_result['playlists']['items'][playnum]['name'] == search_str or "THE SOUND OF "+subgenre.name.upper() == search_str.upper():
                '''playlist name'''
                playlist_name = search_result['playlists']['items'][playnum]['name']
                break

            playlist_name = search_result['playlists']['items'][0]['name']
    else:
        playlist_name = search_result['playlists']['items'][0]['name']

    if playlist_name.upper() != "THE SOUND OF "+subgenre.name.upper() and block == 0:
        raise IndexError("hello")

    '''Get tracks from a playlist'''
    playlist_id = 'spotify:playlist:' + \
        search_result['playlists']['items'][0]['id']

    '''Pulls the playlist tracks'''
    tracks = sp.playlist_items(playlist_id,
                               limit=subgenre.song_amount,
                               offset=offs,
                               fields='items.track.id,total',
                               additional_types=['track'])

    time.sleep(6)

    for s in range(subgenre.song_amount):
        song = Song()

        song.trackid = tracks['items'][s]['track']['id']
        # pprint(song.trackid)

        '''Track Name'''
        song.name = sp.track(song.trackid)
        
        print('\n', song.name['name'])  # Name
        print(song.name['album']['artists'][0]['name'])  # artist
        print(song.name['album']['name'], '\n')  # album

        '''Audio Features'''
        sp.trace = True

        start = time.time()
        song.metadata = sp.audio_features(song.trackid)
        song.popularity

        delta = time.time() - start
        print("features retrieved in %.2f seconds" % (delta,))
        

        song = answerquestion(song)

        data = [[playlist_name, song.name['name'], song.name['album']['artists']
                 [0]['name'], song.name['album']['name'], df['genre'][subg], df['Name'][subg], df['prior_prob'][subg]]]
        dfTwo = pd.DataFrame(data)
        dfTwo.to_csv("test.csv", index=False, mode='a', header=False)
        

if __name__ == "__main__":
    data = [['playlist_name', 'song', 'artist', 'album', 'genre', 'subgenre', 'prior_prob']]
    dfTwo = pd.DataFrame(data)

    dfTwo.to_csv("test.csv", index=False, mode='a', header=False)
    df = pd.read_csv('curated_subgenres_data.csv')
    print(df.head())
    # print(df['Name'][0], df['prior_prob'][0], df['song_amount'][0])

    # subgenres = []

    for subg in range(120):
        subgenre = SubGenre(df['Name'][subg], df['prior_prob'][subg], int(df['song_amount'][subg]))
        
        try:
            print("WORRRRRRRRRRRRRRRRRRRKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
            block = 0
            search_str = 'The Sound of '+subgenre.name  # +' AND The Sounds of Spotify'
            main(search_str, subg, dfTwo, subgenre, block)
        except IndexError:
            print("SHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESHHHSHHHHHHH")
            block = 1
            search_str = subgenre.name
            main(search_str, subg, dfTwo, subgenre, block)
