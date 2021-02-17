import json
import os
from datetime import datetime
from sqlalchemy import create_engine


# local path to json file directory
json_directory = "scraper/json_files"
# youtube url header
youtubeurl = "https://www.youtube.com/watch?v="

# sqlalchemy connect to rds server
rds_connection_string = "postgres:password@postgresdb.cbtoq3riq9z0.us-west-1.rds.amazonaws.com:5432/fivesecondfilms"
engine = create_engine(f'postgresql://{rds_connection_string}')


for filename in os.listdir(json_directory):
    #  filename = os.fsdecode(file)
    if filename.endswith(".json"):
        
        # write full path to json file
        fullpath = json_directory + "/" + str(filename)
        # print(fullpath)
        jsonfile = open(f"{fullpath}", encoding="utf-8")

        # read json file 
        data = json.load(jsonfile)
        
        # pretty print, not that necessary since I can open in notepad++
        # data_pretty = json.dumps(data, indent=2)
        # print(data_pretty)

        # pretty print first video entry
        # data_pretty = json.dumps(data['items'][0], indent=2)
        # print(data_pretty)

        # loop through each video entry in file
        for key in data['items']:
            # print(key['snippet']['description'])

            # video variables
            title = key['snippet']['title']
            timestamp = key['snippet']['publishedAt']
            description = key['snippet']['description']
            thumbnail = key['snippet']['thumbnails']['default']['url']
            videoid = key['snippet']['resourceId']['videoId']

            date = datetime.strptime(timestamp, '%Y-%m-%dT%XZ')

            print(title)
            print(date)
            print(description)
            print(thumbnail)
            print(youtubeurl + videoid)

            # key_pretty = json.dumps(key, indent=2)
            # print(key_pretty)

            


            break


        break # temporary stop to work with only 1 file right now
        #  print(os.path.join(json_directory, filename))
        #  continue
    else:
        continue


# for x in range(42):
#     y = x+1
#     print(y)