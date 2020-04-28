import json
import os
import csv

songs={}

with open('flat_dict.csv', newline='') as csvfile:
    lines=[]
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        lines.append(row)
# print(lines)

for row in range(len(lines)):
    songs[lines[row][5]]={}

with open('unique_songs.json', 'w') as outfile:
   json.dump(songs, outfile)
