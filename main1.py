from urllib.request import urlopen
import folder
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

response = urlopen("https://www.google.com/doodles/json/2018/10?hl=zh_TW")

doodles = json.load(response)

for doodle in doodles:
    url = "https:" + doodle['url']
    print(doodle['title'])
    image_folder_name = "temp"
    folder.create(image_folder_name)
    response = urlopen(url)
    image_file_name = image_folder_name + "/" + url.split("/")[len(url.split("/")) - 1]
    image_file = open(image_file_name, "wb")
    image_file.write(urlopen(url).read())
    image_file.close()
