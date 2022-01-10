import pandas as pd


data = [['playlist_name', 'song', 'artist', 'album', 'genre', 'subgenre', 'prior_prob', 'q1',
            'q2', 'q3', 'q4', 'q5', 'popularity', 'danceability', 'energy', 'loudness', 'valence']]
dfTwo = pd.DataFrame(data)

dfTwo.to_csv("test3.csv", index=False, mode='a', header=False)
df = pd.read_csv('curated_subgenres_data.csv')





data = [[playlist_name, song.name, song.artist, song.album, song.genre, song.subgenre, song.prior_prob, song.questions[0], song.questions[1], song.questions[2],
        song.questions[3], song.questions[4], song.popularity, song.metadata[0]['danceability'], song.metadata[0]['energy'], song.metadata[0]['loudness'], song.metadata[0]['valence']]]
dfTwo = pd.DataFrame(data)
dfTwo.to_csv("test3.csv", index=False, mode='a', header=False)