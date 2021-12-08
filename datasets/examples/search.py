# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'THE SOUND OF TRANCE'
    type_str = 'playlist'
    market_str = None
    limit_int = 1
    offs = 0
    total = 50

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# result = sp.search(search_str, limit_int, offs, type_str, market_str)
result = sp.search_markets(search_str, limit_int,
                           offs, type_str, market_str, total)
pprint.pprint(result)
