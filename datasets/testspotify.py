from __future__ import print_function
# import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
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
        self.name = name
        self.prior_prob = prior_prob
        self.song_amount = song_amount
        self.parent_genre = parent_genre

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

def answerquestion(song):
    '''Q1'''
    if song.popularity > 58:
        song.questions.append('a') #yes
    else:
        song.questions.append('b') #no

    '''Q2'''
    if song.genre == 'World':
        song.questions.append('a') #yes
    else:
        song.questions.append('b') #no

    '''Q3'''
    if song.genre == 'electronic':
        song.questions.append('a')
    elif song.genre == 'rap':
        song.questions.append('b')
    elif song.genre == 'rock':
        song.questions.append('c')
    elif song.genre == 'jazz':
        song.questions.append('d')
    else:
        song.questions.append('e') # Classical

    '''Q4'''
    if song.metadata[0]['instrumentalness'] > 0.5:
        song.questions.append('a') #beats
    else:
        song.questions.append('b') #vocals

    # song.metadata['danceability'] > 0.5 and song.metadata['energy'] > 0.5 and song.metadata['loudness'] > 0.5 and song.metadata['valence'] > 0.9:
    '''Q5'''
    if song.metadata[0]['danceability'] > 0.6 and song.metadata[0]['energy'] > 0.5 and 0.5 < song.metadata[0]['valence']: # 0.5 > valence < 0.8
        song.questions.append('a') #happy
    elif song.metadata[0]['danceability'] < 0.5 and song.metadata[0]['energy'] < 0.3 and song.metadata[0]['valence'] < 0.35:
        song.questions.append('b') #sad
    elif song.metadata[0]['energy'] > 0.79 and 0.1 > song.metadata[0]['valence'] < 0.3:
        song.questions.append('c') #angry
    elif 0.5 < song.metadata[0]['danceability'] < 0.79 and song.metadata[0]['energy'] > 0.8 and 0.6 < song.metadata[0]['valence'] < 0.75: # valence > 0.8
        song.questions.append('d') #hyped
    elif song.metadata[0]['danceability'] > 0.5 and 0.3 < song.metadata[0]['energy'] < 0.7: # 0.4 > valence < 0.6
        song.questions.append('e') #relaxed
    elif 0.4 < song.metadata[0]['danceability'] < 0.6 and 0.59 < song.metadata[0]['energy'] < 0.69 and 0.6 < song.metadata[0]['valence'] < 0.75: # 0.1 > valence < 0.5
        song.questions.append('f') #sensual
    else:
        song.questions.append('z')
    
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
            print(['playlists']['items'][playnum]['name'])
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

    for s in range(3):#range(subgenre.song_amount):
        song = Song(subgenre.parent_genre, subgenre.name, subgenre.prior_prob)

        song.trackid = tracks['items'][s]['track']['id']
        # pprint(song.trackid)

        '''Track Name'''
        track = sp.track(song.trackid)
        song.name = track['name']
        song.artist = track['album']['artists'][0]['name']
        song.album = track['album']['name']

        
        print('\n', song.name)  # Name
        print(song.artist)  # artist
        print(song.album, '\n')  # album

        '''Audio Features'''
        sp.trace = True

        start = time.time()
        song.metadata = sp.audio_features(song.trackid)
        song.popularity = track['popularity']

        print()
        print(song.popularity)
        print(song.metadata[0]['danceability'])
        print(song.metadata[0]['energy'] )
        print(song.metadata[0]['loudness'])
        print(song.metadata[0]['valence'])
        print()

        delta = time.time() - start
        print("features retrieved in %.2f seconds" % (delta,))

        song = answerquestion(song)

        data = [[playlist_name, song.name, song.artist, song.album, song.genre, song.subgenre, song.prior_prob, song.questions[0],song.questions[1],song.questions[2],song.questions[3],song.questions[4],song.popularity,song.metadata[0]['danceability'], song.metadata[0]['energy'],song.metadata[0]['loudness'],song.metadata[0]['valence']]]
        dfTwo = pd.DataFrame(data)
        dfTwo.to_csv("test2.csv", index=False, mode='a', header=False)
        

if __name__ == "__main__":
    data = [['playlist_name', 'song', 'artist', 'album', 'genre', 'subgenre', 'prior_prob', 'q1', 'q2', 'q3', 'q4', 'q5','popularity','danceability','energy','loudness','valence']]
    dfTwo = pd.DataFrame(data)

    dfTwo.to_csv("test2.csv", index=False, mode='a', header=False)
    df = pd.read_csv('curated_subgenres_data.csv')
    print(df.head())
    # print(df['Name'][0], df['prior_prob'][0], df['song_amount'][0])

    # subgenres = []
    

    for subg in range(86,89):
        subgenre = SubGenre(df['Name'][subg], df['prior_prob'][subg], int(df['song_amount'][subg]), df['genre'][subg])
        
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
