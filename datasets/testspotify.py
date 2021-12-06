# import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint




def main():
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = 'track:Lionhearted artist:Porter Robinson'
        type_str = 'track,artist'
        market_str = 'ES'
        limit_int = 5


    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(search_str,limit_int,0,type_str,market_str) #this returns a type dict and is stored in result
    pprint.pprint(result)  

if __name__ == "__main__":
    main()
