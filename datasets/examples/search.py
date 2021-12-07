# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'comedy rock'
    type_str = 'playlist'
    market_str = 'US'
    limit_int = 1
    offs = 0

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str, limit_int, offs, type_str, market_str)
pprint.pprint(result)
