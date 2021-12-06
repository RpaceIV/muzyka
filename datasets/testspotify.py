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

# SubGenre = namedtuple('SubGenre', 'name,')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def main():
    '''Search for a playlist'''
    # if len(sys.argv) > 1:
    #     search_str = sys.argv[1]
    # else:
        # search_str = 'track:Lionhearted artist:Porter Robinson'
        # type_str = 'track,artist'
    search_str = 'playlist:The Sound of breakcore AND The Sounds of Spotify'
    type_str = 'playlist'
    market_str = 'US'
    limit_int = 1
    offs = 0

    result = sp.search(search_str,limit_int,offs,type_str,market_str) #this returns a type dict and is stored in result
    # pprint.pprint(result['playlists']['items'][0]['id'])
    
    '''Get tracks from a playlist'''
    pl_id = 'spotify:playlist:'+result['playlists']['items'][0]['id']
    # pl_id = 'spotify:playlist:5RIbzhG2QqdkaP24iXLnZX'
    # print()
    offset = 0

    # for s in range(6):
    response = sp.playlist_items(pl_id,
                                limit=6,
                                offset=offset,
                                fields='items.track.id,total',
                                additional_types=['track'])
    # if len(response['items']) == 0:
    #     break
    
    # pprint(response['items'])
    for s in range(6):
    #     pprint(response['items'][x]['track']['id'])
        pprint(response['items'][s]['track']['id'])
        # offset = offset + len(response['items'])
        # print(offset, "/", response['total'])

        '''Track Name'''
        trackk = sp.track(response['items'][s]['track']['id'])
        print(trackk['name'])
        print(trackk['album']['artists'][0]['name'])
        print(trackk['album']['name'])
        

        '''Audio Features'''
        sp.trace = True
        # if len(sys.argv) > 1:
        # tids = sys.argv[1:]
        # print(tids)

        start = time.time()
        features = sp.audio_features(response['items'][s]['track']['id'])
        delta = time.time() - start
        print(json.dumps(features, indent=4))
        print("features retrieved in %.2f seconds" % (delta,))

if __name__ == "__main__":
    main()
