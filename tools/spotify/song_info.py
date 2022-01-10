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


def main():
    '''Search for a playlist'''
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = 'track:Uptown Funk artist:Mark Ronson'
        type_str = 'track,artist'
        # search_str = 'playlist:The Sound of breakcore AND The Sounds of Spotify'
        # type_str = 'playlist'
        market_str = 'US'
        limit_int = 1

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(search_str,limit_int,0,type_str,market_str) #this returns a type dict and is stored in result


    '''Get tracks from a playlist'''
    pl_id = 'spotify:track:'+result['tracks']['items'][0]['id'] #'spotify:playlist:5RIbzhG2QqdkaP24iXLnZX'

    offset = 0

    '''Track Name'''

    trackk = sp.track(pl_id)
    print(trackk)
    print(trackk['popularity'])
    print(trackk['name'])
    print(trackk['album']['artists'][0]['name'])
    print(trackk['album']['name'])
    
    print()

    '''Audio Features'''
    sp.trace = True

    start = time.time()
    features = sp.audio_features(pl_id)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    print("features retrieved in %.2f seconds" % (delta,))
    print(features[0]['energy'])

if __name__ == "__main__":
    main()
