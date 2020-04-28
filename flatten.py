import json
import os
import csv


with open('dict.json', encoding="utf8") as f:
    dict=json.load(f)

# flatWriter = csv.writer(open('flat_dict.csv', 'w', newline=''), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
flatWriter = csv.writer(open('flat_dict.csv', 'w', newline=''), delimiter=',')
for record in dict:
    date=[record][0]
    # print(date)
    # print(dict[record])
    for song in dict[record]:
        # pos,track,artist,streams,url
        # for k,v in song:
        # print(str(song))
        # print(dict[record][song])
        # for val in song:
        pos=dict[record][song]['position']
        track=dict[record][song]['track']
        artist=dict[record][song]['artist']
        streams=dict[record][song]['streams']
        url=dict[record][song]['url']

        # try:
        #     track.encode('ascii')
        # except UnicodeDecodeError:
        #     print('track not in ascii')
        #     continue
        #
        # try:
        #     artist.encode('ascii')
        # except UnicodeDecodeError:
        #     print('artist not in ascii')
        #     continue


        # print(date,pos,track,artist,streams,url)
        try:
            flatWriter.writerow([date,pos,track,artist,streams,url])
        except UnicodeEncodeError:
            print('contained characters not compatible with csv file')
            continue
        # flatWriter.writerow([date,pos,track.encode('utf-8'),artist.encode('utf-8'),streams,url])
        # flatWriter.writerow(date,song[0],song[1],song[2],song[3],song[4])
        # flatWriter.writerow(dict[record][0],song['position'],song['track'],song['artist'],song['streams'],song['url'])


# spamWriter = csv.writer(open('eggs.csv', 'w', newline=''), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
