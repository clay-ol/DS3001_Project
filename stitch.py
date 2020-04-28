import json
import os
import csv
path=os.path.abspath(os.path.dirname(__file__)) + '/allData/'
dates=[]
with open('dates_all.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        dates.append(row)


# os.chdir(os.path.abspath(os.path.dirname(__file__)) + '/allData')
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#declare the dictionary
data={}
params=['position','track','artist','streams','url']
# dates=[['2017-01-01']]
#first loop through each of the dates
for row in range(len(dates)):
    # print(row)
    c_date=str(dates[row][0])
    # print(c_date)
    day_file=path+c_date+'.csv'
    # print(day_file)
    # data[c_date]=[]
    titles={}
    with open(day_file,newline='', encoding="utf8") as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        # reader=csv.DictReader(csvfile,fieldnames=params,delimiter=',')

        line1=next(reader)
        # line1_item=str(line1['position'])
        line1_item=str(line1[0])
        # print(str(line1_item))
        if(line1_item=='<!doctype html>'):
            print('true')
            continue
        next(reader)
        # print(reader)
        for row2 in reader:
            song={}
            song['position']=row2[0]
            song['track']=row2[1]
            song['artist']=row2[2]
            song['streams']=row2[3]
            song['url']=row2[4]
            # titles.append(row2)
            # print(str(row2))
            # print(row2[0])
            titles[row2[0]]=song
    # print(titles)
    data[c_date]=titles
    titles={}




#save dictionary to json
with open('dict.json', 'w') as outfile:
   json.dump(data, outfile)
