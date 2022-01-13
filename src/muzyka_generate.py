from __future__ import print_function
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
from collections import namedtuple

import json
import time
import sys
import pandas as pd


# SubGenre = namedtuple('SubGenre', 'name,prior_prob,song_amount')
# SongInfo = namedtuple('SongInfo', 'song,artist,album,main_genre,subgenre,prior_prob,q1,q2,q3,q4,q5')


class SubGenre:
    def __init__(self, name, prior_prob, song_amount, parent_genre):
        self.name = name
        self.prior_prob = prior_prob
        self.song_amount = song_amount
        self.parent_genre = parent_genre


class Song:
    def __init__(self, maing, subg, prior_prob):
        self.maing = maing
        self.subg = subg
        self.prior_prob = prior_prob

        self.name = ''
        self.artist = ''
        self.album = ''

        self.questions = []  # list of questions

        self.trackid = 0
        self.popularity = 0
        self.metadata = dict()

def fillSongData(row_data):
    songDF = pd.DataFrame(row_data)
    songDF.to_csv("datasets/csv_data/song_data_out.csv", index=False, mode='a', header=False)


def answerquestion(song):
    '''Q1'''
    if song.popularity > 58:
        song.questions.append(1)  # yes
    else:
        song.questions.append(2)  # no

    '''Q2'''
    if song.maing == 'World':
        song.questions.append(1)  # yes
    else:
        song.questions.append(2)  # no

    '''Q3'''
    if song.maing == 'electronic':
        song.questions.append(1)
    elif song.maing == 'rap':
        song.questions.append(2)
    elif song.maing == 'rock':
        song.questions.append(3)
    elif song.maing == 'jazz':
        song.questions.append(4)
    else:
        song.questions.append(5)  # Classical

    '''Q4'''
    if song.metadata[0]['instrumentalness'] > 0.5:
        song.questions.append(1)  # beats
    else:
        song.questions.append(2)  # vocals

    '''Q5'''
    if song.maing == "electronic":
        if song.metadata[0]['danceability'] > 0.6 and song.metadata[0]['energy'] > 0.5 and 0.4 < song.metadata[0]['valence']:  # 0.5 > valence < 0.8
            song.questions.append(1)  # happy
        elif song.metadata[0]['danceability'] < 0.5 and song.metadata[0]['energy'] < 0.4 and song.metadata[0]['valence'] < 0.35:
            song.questions.append(2)  # sad
        elif song.metadata[0]['energy'] > 0.7 and 0.1 < song.metadata[0]['valence'] < 0.45:
            song.questions.append(3)  # angry
        elif song.metadata[0]['danceability'] < 0.79 and song.metadata[0]['energy'] > 0.8 and song.metadata[0]['valence'] < 0.75:  # valence > 0.8
            song.questions.append(4)  # hyped
        elif song.metadata[0]['danceability'] > 0.5 and 0.3 < song.metadata[0]['energy'] < 1.0:
            song.questions.append(5)  # relaxed
        elif 0.2 < song.metadata[0]['danceability'] < 0.6 and 0.59 < song.metadata[0]['energy'] and 0.6 < song.metadata[0]['valence'] < 0.75:
            song.questions.append(6)  # sensual
        else:
            song.questions.append('z')
    elif song.maing == "rap":
        if song.metadata[0]['danceability'] > 0.6 and song.metadata[0]['energy'] > 0.5 and 0.4 < song.metadata[0]['valence']:  # 0.5 > valence < 0.8
            song.questions.append(1)  # happy
        elif song.metadata[0]['danceability'] < 0.5 and song.metadata[0]['energy'] < 0.3 and song.metadata[0]['valence'] < 0.35:
            song.questions.append(2)  # sad
        elif song.metadata[0]['energy'] > 0.79 and 0.1 > song.metadata[0]['valence'] < 0.3:
            song.questions.append(3)  # angry
        elif 0.5 < song.metadata[0]['danceability'] < 0.79 and song.metadata[0]['energy'] > 0.8 and 0.6 < song.metadata[0]['valence'] < 0.75:  # valence > 0.8
            song.questions.append(4)  # hyped
        elif song.metadata[0]['danceability'] > 0.4 and 0.3 < song.metadata[0]['energy'] < 1.0:
            song.questions.append(5)  # relaxed
        elif song.metadata[0]['danceability'] < 0.6 and 0.5 < song.metadata[0]['energy'] < 0.8 and song.metadata[0]['valence'] < 0.75:
            song.questions.append(6)  # sensual
        else:
            song.questions.append('z')
    elif song.maing == "rock":
        if song.metadata[0]['danceability'] > 0.6 and song.metadata[0]['energy'] > 0.5 and 0.5 < song.metadata[0]['valence']:  # 0.5 > valence < 0.8
            song.questions.append(1)  # happy
        elif song.metadata[0]['danceability'] < 0.5 and song.metadata[0]['energy'] < 0.3 and song.metadata[0]['valence'] < 0.35:
            song.questions.append(2)  # sad
        elif song.metadata[0]['energy'] > 0.79 and 0.1 > song.metadata[0]['valence'] < 0.3:
            song.questions.append(3)  # angry
        elif song.metadata[0]['danceability'] < 0.8 and song.metadata[0]['energy'] > 0.7 and song.metadata[0]['valence'] < 0.75:
            song.questions.append(4)  # hyped
        elif song.metadata[0]['danceability'] > 0.5 and 0.3 < song.metadata[0]['energy'] < 0.7:
            song.questions.append(5)  # relaxed
        elif 0.1 < song.metadata[0]['danceability'] < 0.7 and song.metadata[0]['energy'] < 0.8 and 0.6 < song.metadata[0]['valence'] < 0.8:
            song.questions.append(6)  # sensual
        else:
            song.questions.append('z')
    elif song.maing == "jazz":
        if song.metadata[0]['danceability'] > 0.5 and song.metadata[0]['energy'] < 0.5 and song.metadata[0]['valence'] < 0.8:  # 0.5 > valence < 0.8
            song.questions.append(1)  # happy
        elif song.metadata[0]['danceability'] < 0.6 and song.metadata[0]['energy'] < 0.3 and song.metadata[0]['valence'] < 0.6:
            song.questions.append(2)  # sad
        elif song.metadata[0]['energy'] > 0.7 and 0.1 > song.metadata[0]['valence'] < 0.3:
            song.questions.append(3)  # angry
        elif song.metadata[0]['danceability'] < 0.79 and song.metadata[0]['energy'] > 0.8 and song.metadata[0]['valence'] < 0.75:  # valence > 0.8
            song.questions.append(4)  # hyped
        elif song.metadata[0]['danceability'] > 0.5 and 0.3 < song.metadata[0]['energy'] < 0.7:
            song.questions.append(5)  # relaxed
        elif song.metadata[0]['danceability'] < 0.8 and song.metadata[0]['energy'] < 0.7 and song.metadata[0]['valence'] < 1.0:
            song.questions.append(6)  # sensual
        else:
            song.questions.append('z')
    elif song.maing == "classical":
        if song.metadata[0]['danceability'] > 0.6 and song.metadata[0]['energy'] > 0.5 and 0.5 < song.metadata[0]['valence']:  # 0.5 > valence < 0.8
            song.questions.append(1)  # happy
        elif song.metadata[0]['danceability'] < 0.5 and song.metadata[0]['energy'] < 0.3 and song.metadata[0]['valence'] < 0.35:
            song.questions.append(2)  # sad
        elif song.metadata[0]['energy'] > 0.79 and song.metadata[0]['valence'] < 0.3:
            song.questions.append(3)  # angry
        elif song.metadata[0]['danceability'] < 0.79 and song.metadata[0]['energy'] > 0.6 and song.metadata[0]['valence'] < 0.75:  # valence > 0.8
            song.questions.append(4)  # hyped
        elif song.metadata[0]['danceability'] > 0.5 and song.metadata[0]['energy'] < 0.7:
            song.questions.append(5)  # relaxed
        elif song.metadata[0]['danceability'] < 0.6 and song.metadata[0]['energy'] < 0.69 and song.metadata[0]['valence'] < 0.75:
            song.questions.append(6)  # sensual
        else:
            song.questions.append('z')
    elif song.maing == "world":
        if song.metadata[0]['danceability'] > 0.6 and song.metadata[0]['energy'] > 0.5 and 0.4 < song.metadata[0]['valence']:  # 0.5 > valence < 0.8
            song.questions.append(1)  # happy
        elif song.metadata[0]['danceability'] < 0.6 and song.metadata[0]['energy'] < 1.0 and song.metadata[0]['valence'] < 0.6:
            song.questions.append(2)  # sad
        elif song.metadata[0]['energy'] > 0.7 and song.metadata[0]['valence'] < 0.5:
            song.questions.append(3)  # angry
        elif song.metadata[0]['danceability'] < 0.7 and song.metadata[0]['energy'] > 0.7 and song.metadata[0]['valence'] < 1.0:  # valence > 0.8
            song.questions.append(4)  # hyped
        elif song.metadata[0]['danceability'] > 0.5 and song.metadata[0]['energy'] < 0.7:
            song.questions.append(5)  # relaxed
        elif song.metadata[0]['danceability'] < 0.6 and song.metadata[0]['energy'] < 0.7 and song.metadata[0]['valence'] < 1.0:
            song.questions.append(6)  # sensual
        else:
            song.questions.append('z')
    else:
        print("Fail.")
    return song


def main(preferred_playlist, subg, not_preferred):
    search_key = 'playlist'
    iso_alpha2_code = 'US'
    queue_limit = 20
    offset = 0

    '''searches for the playlist'''
    search_result = spotAPI.search(preferred_playlist, queue_limit,
                              offset, search_key, iso_alpha2_code)

    '''Searches search results and selects the playlist'''
    #This condition block consists of a first result of the nonpreferred_playlist being chosen and the second
    #result being the preferred_playlist chosen
    if len(search_result['playlists']['items'][0]['name']) > len(preferred_playlist) and not_preferred == 1:
        for p in range(queue_limit-1):
            if search_result['playlists']['items'][p]['name'] == preferred_playlist or "THE SOUND OF "+subg.name.upper() == preferred_playlist.upper():
                playlist_name = search_result['playlists']['items'][p]['name']
                break

            playlist_name = search_result['playlists']['items'][0]['name']
    else:
        playlist_name = search_result['playlists']['items'][0]['name']

    #This will only trigger on the first run for when we could not get the preferred playlist as the top result.
    #On the second run we will select the second best playlist.
    if playlist_name.upper() != "THE SOUND OF "+subg.name.upper() and not_preferred == 0:
        raise IndexError("hello")

    '''Get tracks from a playlist'''
    playlist_id = 'spotify:playlist:' + \
        search_result['playlists']['items'][0]['id']

    '''Pulls the playlist tracks'''
    tracks = spotAPI.playlist_items(playlist_id,
                               limit=subg.song_amount,
                               offset=offset,
                               fields='items.track.id,total',
                               additional_types=['track'])


    for s in range(subg.song_amount):  # range(subg.song_amount):
        song = Song(subg.parent_genre, subg.name, subg.prior_prob)
        song.trackid = tracks['items'][s]['track']['id']

        '''Track Name'''
        track = spotAPI.track(song.trackid)
        song.name = track['name']
        song.artist = track['album']['artists'][0]['name']
        song.album = track['album']['name']

        print('\n', song.name)  # Name
        print(song.artist)  # artist
        print(song.album, '\n')  # album

        '''Audio Features'''
        spotAPI.trace = True
        song.metadata = spotAPI.audio_features(song.trackid)
        song.popularity = track['popularity']

        print()
        print(song.popularity)
        print(song.metadata[0]['danceability'])
        print(song.metadata[0]['energy'])
        print(song.metadata[0]['loudness'])
        print(song.metadata[0]['valence'])
        print()

        song = answerquestion(song)

        table_body = [[playlist_name, song.name, song.artist, song.album, song.maing, song.subg, song.prior_prob, song.questions[0], song.questions[1], song.questions[2],
                 song.questions[3], song.questions[4], song.popularity, song.metadata[0]['danceability'], song.metadata[0]['energy'], song.metadata[0]['loudness'], song.metadata[0]['valence']]]
        
        fillSongData(table_body)

    #Pause 6 seconds to not overflow spotify api
    time.sleep(6)


if __name__ == "__main__":
    spotAPI = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    subg_amount = 120

    subgDF = pd.read_csv('datasets/csv_data/subgenres_data.csv')
    print(subgDF.head())

    table_header = [['playlist_name', 'song', 'artist', 'album', 'main_genre', 'subgenre', 'prior_prob', 'q1',
            'q2', 'q3', 'q4', 'q5', 'popularity', 'danceability', 'energy', 'loudness', 'valence']]
    fillSongData(table_header)


    for g in range(subg_amount):
        subg = SubGenre(subgDF['Name'][g], subgDF['prior_prob'][g], int(subgDF['song_amount'][g]), subgDF['main_genre'][g])
        try:
            not_preferred = 0
            preferred_playlist = 'The Sound of '+subg.name
            main(preferred_playlist, subg, not_preferred)
        except IndexError:
            not_preferred = 1
            preferred_playlist = subg.name
            main(preferred_playlist, subg, not_preferred)
