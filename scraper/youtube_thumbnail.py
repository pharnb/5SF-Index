import requests
import json
import os

json_directory = "scripts/data.json"
jsonfile = open(f"{json_directory}", encoding="utf-8")

data = json.load(jsonfile)

for key in data:
    imageurl = key['thumbnail']
    imagepath = imageurl[22:]
    imagepath = imagepath[:12]
    # print(imagepath)
    # print("-----------")

    if not os.path.exists(f"E:/GitHub/5SF-Index/test{imagepath}"):
        try:
            os.makedirs(f"E:/GitHub/5SF-Index/test{imagepath}")
            # print("created folder")
        except:
            
            continue
    # else:
        # print("already folder")


    r = requests.get(imageurl, allow_redirects=True)
    open(f"E:/GitHub/5SF-Index/test{imagepath}/default.jpg", 'wb').write(r.content)
    # print("done")
    # print("-----------")


    # break
