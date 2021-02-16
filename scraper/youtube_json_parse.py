import json
import os

json_directory = 'scraper\json_files'

for filename in os.listdir(json_directory):
    #  filename = os.fsdecode(file)
    if filename.endswith(".json"):
        fullpath = json_directory + "/" + str(filename)
        print(fullpath)
        jsonfile = open(f"{fullpath}", encoding="utf-8")
        data = json.load(jsonfile)
        print(data)
        break
        #  print(os.path.join(json_directory, filename))
        #  continue
    else:
        continue


# for x in range(42):
#     y = x+1
#     print(y)