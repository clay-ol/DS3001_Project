import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

c_id = 'bf02bcb1126f4363b3a4a057c623d182'
c_secret = '6c563e24a4ff4700a2e25adc0a662d80'

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=c_id, client_secret=c_secret))

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])



# Meta Data that will be harvested for each song
# Top Genre
# Year
# BPM
# Energy
# Dance
# loudness
# liveness
# valence
# mode
# speachiness
# acousticness
# instrumentalness
# tempo
# duration_ms

# metaList = []
urlLists = []
metaList = {}


with open('unique_songs.json', encoding="utf8") as f:
    dict=json.load(f)

urltempList = list( dict.keys() )

x = 0
y = len( urltempList )

# for i in range(x, y, 100):
#     # takes in a comma delimited list of IDs up to 100 IDs
#     trackMetas = spotify.audio_features( urltempList[x:x+100] )
#     metaList.append( trackMetas )
#     x+=100   
for i in range(x, y,100):
    # print( i )
    # print (urltempList[x:x+100] )
    trackMetas = spotify.audio_features( urltempList[x:x+100] )
    for row in range(len(trackMetas)):
        metaList[urltempList[x+row]]=trackMetas[row]
    x+=100


# write song meta data to a json for further use
with open( 'songMeta.json', 'w' ) as outfile:
    json.dump( metaList, outfile )

