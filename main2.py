from urllib.request import urlopen
from urllib.request import urlretrieve
import folder
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

response = urlopen("https://www.google.com/doodles/json/2018/10?hl=zh_TW")

doodles = json.load(response)

for doodle in doodles:
    url = "https:" + doodle['url']
    print(doodle['title'])
    folder.create("temp")
    filename = "temp/" + url.split("/")[len(url.split("/")) - 1]
    urlretrieve(url, filename)
