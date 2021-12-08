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

SubGenre = namedtuple('SubGenre', 'name,prior_prob,song_amount')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def main(search_str, subg, dfTwo, subgenre, block):

    # TODO fill in this with corresponding cell of the excel sheet

    # for i in range(len(subgenre)):
    # print('\n', df['Name'][i], df['prior_prob']
    #       [i], df['song_amount'][i], '\n')
    # print(1)
    # subgenre = SubGenre(df['Name'][i], df['prior_prob']
    #                     [i], int(df['song_amount'][i]))
    '''Search for a playlist'''
    # if len(sys.argv) > 1:
    #     search_str = sys.argv[1]
    # else:
    # search_str = 'track:Lionhearted artist:Porter Robinson'
    # type_str = 'track,artist'

    type_str = 'playlist'
    market_str = 'US'
    limit_int = 50
    offs = 0

    search_result = sp.search(search_str, limit_int,
                              offs, type_str, market_str)

    if len(search_result['playlists']['items'][0]['name']) > len(search_str) and block == 1:
        for playnum in range(limit_int-1):
            if search_result['playlists']['items'][playnum]['name'] == search_str or "THE SOUND OF "+subgenre.name.upper() == search_str.upper():
                '''playlist name'''
                playlist_name = search_result['playlists']['items'][playnum]['name']
                break

            playlist_name = search_result['playlists']['items'][0]['name']
    else:
        playlist_name = search_result['playlists']['items'][0]['name']

        # this returns a type dict and is stored in result

        # pprint.pprint(result['playlists']['items'][0]['id'])

    '''Get tracks from a playlist'''
    playlist_id = 'spotify:playlist:' + \
        search_result['playlists']['items'][0]['id']

    print(block)

    if playlist_name.upper() != "THE SOUND OF "+subgenre.name.upper() and block == 0:
        raise IndexError("hello")
    # pl_id = 'spotify:playlist:5RIbzhG2QqdkaP24iXLnZX'
    # print()
    offset = 0

    # for s in range(6):
    tracks = sp.playlist_items(playlist_id,
                               limit=subgenre.song_amount,
                               offset=offset,
                               fields='items.track.id,total',
                               additional_types=['track'])
    # if len(response['items']) == 0:
    #     break
    # pprint(response['items'])
    time.sleep(6)
    for s in range(subgenre.song_amount):
        # print(s)
        track_id = tracks['items'][s]['track']['id']
    #     pprint(response['items'][x]['track']['id'])
        pprint(track_id)
        # offset = offset + len(response['items'])
        # print(offset, "/", response['total'])

        '''Track Name'''
        track = sp.track(track_id)
        data = [[playlist_name, track['name'], track['album']['artists']
                 [0]['name'], track['album']['name'], df['genre'][subg], df['Name'][subg], df['prior_prob'][subg]]]
        dfTwo = pd.DataFrame(data)
        dfTwo.to_csv("test.csv", index=False, mode='a',
                     header=False)
        print('\n', track['name'])  # Name
        print(track['album']['artists'][0]['name'])  # artist
        print(track['album']['name'], '\n')  # album

        '''Audio Features'''
        sp.trace = True
        # if len(sys.argv) > 1:
        # tids = sys.argv[1:]
        # print(tids)

        start = time.time()
        track_features = sp.audio_features(track_id)
        delta = time.time() - start
        # print(json.dumps(track_features, indent=4))
        print("features retrieved in %.2f seconds" % (delta,))


if __name__ == "__main__":
    data = [['playlist_name', 'song', 'artist',
             'album', 'genre', 'subgenre', 'prior_prob']]
    dfTwo = pd.DataFrame(data)
    dfTwo.to_csv("test.csv", index=False, mode='a',
                 header=False)

    df = pd.read_csv('curated_subgenres_data.csv')
    print(df.head())
    # print(df['Name'][0], df['prior_prob'][0], df['song_amount'][0])

    subgenres = []

    for subg in range(120):
        try:
            print("WORRRRRRRRRRRRRRRRRRRKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
            block = 0
            subgenre = SubGenre(df['Name'][subg], df['prior_prob']
                                [subg], int(df['song_amount'][subg]))
            search_str = 'The Sound of '+subgenre.name  # +' AND The Sounds of Spotify'
            main(search_str, subg, dfTwo, subgenre, block)
        except IndexError:
            print("SHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESHHHSHHHHHHH")
            block = 1
            subgenre = SubGenre(df['Name'][subg], df['prior_prob']
                                [subg], int(df['song_amount'][subg]))
            search_str = subgenre.name
            main(search_str, subg, dfTwo, subgenre, block)
