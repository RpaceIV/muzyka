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

# SubGenre = namedtuple('SubGenre', 'name,prior_prob,song_amount')
# SongInfo = namedtuple('SongInfo', 'song,artist,album,genre,subgenre,prior_prob,q1,q2,q3,q4,q5')

class SubGenre:
    def __init__(self,name,prior_prob,song_amount):
        self.name = name
        self.prior_prob = prior_prob
        self.song_amount = song_amount

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# def answerquestions():



def main():

    df = pd.read_csv('curated_subgenres_data.csv')
    # print(df.head())
    # subgenres = []

    subgenre = SubGenre("", 0.0, 0) 

    for subg in range(1):
        print(df['Name'][subg])

        # subgenre = SubGenre(df['Name'][subg], 
        #                     df['prior_prob'][subg], 
        #                     int(df['song_amount'][subg])) 
        
        subgenre.name = df['Name'][subg] 
        subgenre.prior_prob = df['prior_prob'][subg] 
        subgenre.song_amount = int(df['song_amount'][subg]) 

        '''Search for a playlist'''
        search_str = 'playlist:The Sound of '+subgenre.name+' AND The Sounds of Spotify'
        type_str = 'playlist'
        market_str = 'US'
        limit_int = 1
        offs = 0

        # this returns a type dict and is stored in result
        search_result = sp.search(search_str, 
                                  limit_int, 
                                  offs, 
                                  type_str, 
                                  market_str)
        
        '''Get tracks from a playlist'''
        playlist_id = 'spotify:playlist:' + search_result['playlists']['items'][0]['id']
        offset = 0

        tracks = sp.playlist_items(playlist_id,
                                   limit=subgenre.song_amount,
                                   offset=offset,
                                   fields='items.track.id,total',
                                   additional_types=['track'])
        
        for s in range(subgenre.song_amount):
            track_id = tracks['items'][s]['track']['id']
            pprint(track_id)
        
            '''Track Name'''
            track = sp.track(track_id)
            # print(track)
            print('\n', track['name'])  # Name
            print(track['album']['artists'][0]['name'])  # artist
            print(track['album']['name'], '\n')  # album

            '''Audio Features'''
            sp.trace = True
        
            start = time.time()
            track_features = sp.audio_features(track_id)
            delta = time.time() - start
            print(json.dumps(track_features, indent=4))
            print("features retrieved in %.2f seconds" % (delta,))


if __name__ == "__main__":
    main()
