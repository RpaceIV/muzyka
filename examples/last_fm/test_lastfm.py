import pylast
import lastFMDesc as desc

network = pylast.LastFMNetwork(
    api_key=desc.API_KEY,
    api_secret=desc.API_SECRET,
    username=desc.username,
    password_hash=desc.password_hash,
)

tag = pylast.Tag("electronic", network)
tagTopTracks = tag.get_top_tracks(limit=10)
for index in tagTopTracks:
    print(index[0])

# Now you can use that object everywhere
# track = network.get_track("DPR Live", "Text Me")
# print(track.title)
# artist = network.get_artist()
# tag = network.get_tag("DPR Live")
# topArtist = network.get_top_artists()
# print(artist.get_top_albums())
# print(artist.get_bio("content"))
# print(topArtist)
# track.love()
# track.add_tags(("awesome", "favorite"))


# track = pylast.Track("DPR Live", "Jasmine", network)

# for pylast.Track in artist.get_top_tracks(limit=1):
#     print(pylast.Track.title)
# artist = pylast.Artist("DPR Live", network)
# artistTopTracks = artist.get_top_tracks(limit=2)
# print(artistTopTracks[0][0].title)

# print(tagTopTracks[0][0].title)
# for index in tagTopTracks:
#     artistName = index[0].artist
#     topTrackTitle = index[0].title
#     print(artistName)
#     print(topTrackTitle)


# for index in tagTopTracks:
#     print(index[0].artist)

# for index in tagTopTracks:
#     print(index[0].title)

# print(pylast.Track("DPR Live", "Jasmine", network))

# for title in track:
#     print(title)

# tag = pylast.Tag(None, network)
# print(tag.get_top_artists())
