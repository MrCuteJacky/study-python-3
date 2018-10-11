from urllib.request import urlopen
from urllib.request import urlretrieve
import folder
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


for year in range(2018, 2019):
    print("Start download " + str(year) + " year.")
    for month in range(1, 13):
        print("Start download " + str(year) + "年" + str(month) + "月.")
        response = urlopen("https://www.google.com/doodles/json/" + str(year) + "/" + str(month) + "?hl=zh_TW")
        doodles = json.load(response)
        for doodle in doodles:
            url = "https:" + doodle['url']
            print(doodle['title'])
            folder_name = "doodles_" + str(year) + "_" + str(month)
            folder.create(folder_name)
            file_name = folder_name + "/" + url.split("/")[len(url.split("/")) - 1]
            urlretrieve(url, file_name)
print("Finish!!!")
