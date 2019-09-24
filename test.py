# -*- coding: UTF-8 -*-
import urllib.request, json
from selenium import webdriver

api_key = "??????"
channel_id =  "UCWr0mx597DnSGLFk1WfvSkQ"
base_search_url = "https://www.googleapis.com/youtube/v3/search?"
url = base_search_url + "key={}&channelId={}&part=snippet,id&order=date&maxResults=1".format(api_key, channel_id)

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

#url = "https://www.wikipedia.com"

page = urllib.request.urlopen(url)
resp = json.load(page)
#inp = urllib.request.urlopen(page).read()

print(resp)

#resp = json.load(inp.)
vidID = resp['items'][0]['id']['videoId']
print(vidID)

#driver = webdriver.Safari()
#base_video_url = "https://www.youtube.com/watch?v="
#driver.get( base_video_url + vidID)


# https://www.googleapis.com/youtube/v3/search?key=??????&channelId=UCWr0mx597DnSGLFk1WfvSkQ&part=snippet,id&order=date&maxResults=1




#request = request = urllib.request.Request(url, headers=headers)
#resp = urllib.request.urlopen(request)