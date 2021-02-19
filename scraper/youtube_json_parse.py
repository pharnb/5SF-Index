import json
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# define youtube data table
class youtube(Base):
    __tablename__ = 'youtubedata'
    title = Column(String, primary_key=True)
    date = Column(String)
    description = Column(String)
    thumbnail = Column(String)
    url = Column(String)


# local path to json file directory
json_directory = "scraper/json_files"
# youtube url header
youtubeurl = "https://www.youtube.com/watch?v="

# sqlalchemy connect to rds server
# rds_connection_string imported
from miscvar import *
engine = create_engine(f'postgresql://{rds_connection_string}')
session = Session(engine)



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
            url = youtubeurl + videoid

            date = datetime.strptime(timestamp, '%Y-%m-%dT%XZ')

            print(filename)
            print(title)
            # print(date)
            # print(description)
            # print(thumbnail)
            # print(url)
            print("--------------------")

            # key_pretty = json.dumps(key, indent=2)
            # print(key_pretty)

            session.add(youtube(title=title, date=date, description=description, thumbnail=thumbnail, url=url))

            session.new
            session.commit()


            # break


        # break # temporary stop to work with only 1 file right now
        #  print(os.path.join(json_directory, filename))
        #  continue
    else:
        continue


# for x in range(42):
#     y = x+1
#     print(y)