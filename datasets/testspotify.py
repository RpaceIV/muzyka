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

SubGenre = namedtuple('SubGenre', 'name,prior_prob,song_amount')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def main():

    subgenres = []

    for subg in range(120):
        subgenre = SubGenre('',,) #TODO fill in this with corresponding cell of the excel sheet

        '''Search for a playlist'''
        # if len(sys.argv) > 1:
        #     search_str = sys.argv[1]
        # else:
            # search_str = 'track:Lionhearted artist:Porter Robinson'
            # type_str = 'track,artist'
        search_str = 'playlist:The Sound of '+subgenre.name+' AND The Sounds of Spotify'
        type_str = 'playlist'
        market_str = 'US'
        limit_int = 1
        offs = 0

        search_result = sp.search(search_str,limit_int,offs,type_str,market_str) #this returns a type dict and is stored in result
        # pprint.pprint(result['playlists']['items'][0]['id'])
        
        '''Get tracks from a playlist'''
        playlist_id = 'spotify:playlist:'+search_result['playlists']['items'][0]['id']
        # pl_id = 'spotify:playlist:5RIbzhG2QqdkaP24iXLnZX'
        # print()
        offset = 0

        # for s in range(6):
        tracks = sp.playlist_items(playlist_id,
                                    limit=6,
                                    offset=offset,
                                    fields='items.track.id,total',
                                    additional_types=['track'])
        # if len(response['items']) == 0:
        #     break
        
        # pprint(response['items'])
        for s in range(subgenre.song_amount):
            track_id = tracks['items'][s]['track']['id']
        #     pprint(response['items'][x]['track']['id'])
            pprint(track_id)
            # offset = offset + len(response['items'])
            # print(offset, "/", response['total'])

            '''Track Name'''
            track = sp.track(track_id)
            print(track['name']) #Name
            print(track['album']['artists'][0]['name']) #artist
            print(track['album']['name']) #album
            

            '''Audio Features'''
            sp.trace = True
            # if len(sys.argv) > 1:
            # tids = sys.argv[1:]
            # print(tids)

            start = time.time()
            track_features = sp.audio_features(track_id)
            delta = time.time() - start
            print(json.dumps(track_features, indent=4))
            print("features retrieved in %.2f seconds" % (delta,))

if __name__ == "__main__":
    main()
