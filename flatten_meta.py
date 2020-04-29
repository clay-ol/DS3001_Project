import json
import os
import csv


with open('songMeta.json', encoding="utf8") as f:
    dict=json.load(f)

# for record in dict:
#     date=[record][0]
#     for song in dict[record]:
#         pos=dict[record][song]['position']

# flatWriter = csv.writer(open('flat_dict.csv', 'w', newline=''), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
flatWriter = csv.writer(open('flat_meta.csv', 'w', newline=''), delimiter=',')
for record in dict:
    track_ref=[record][0]
    danceability=dict[record]['danceability']
    energy=dict[record]['energy']
    key=dict[record]['key']
    loudness=dict[record]['loudness']
    mode=dict[record]['mode']
    speechiness=dict[record]['speechiness']
    acousticness=dict[record]['acousticness']
    instrumentalness=dict[record]['instrumentalness']
    liveness=dict[record]['liveness']
    valence=dict[record]['valence']
    tempo=dict[record]['tempo']
    type=dict[record]['type']
    id=dict[record]['id']
    uri=dict[record]['uri']
    analysis_url=dict[record]['analysis_url']
    duration_ms=dict[record]['duration_ms']
    time_signature=dict[record]['time_signature']

    flatWriter.writerow([track_ref,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,type,id,uri,analysis_url,duration_ms,time_signature])