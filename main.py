# -*- coding: UTF-8 -*-

import os 	# Necessary for env variables
import urllib.request, json
from selenium import webdriver # pip install selinium for this package to work
import time

def look_for_new_video():
	api_key = os.environ.get('API_KEY_YOUTUBE')# whatever your api key is get it here: http://console.developers.google.com
	channel_id =  "UCWr0mx597DnSGLFk1WfvSkQ" # get the channerl id for whatever channel you want to track"

	base_video_url = "https://www.youtube.com/watch?v="
	base_search_url = "https://www.googleapis.com/youtube/v3/search?"
	
	url = base_search_url + "key={}&channelId={}&part=snippet,id&order=date&maxResults=1".format(api_key, channel_id)
	
	inp = urllib.request.urlopen(url)

	resp = json.load(inp)
	
	# print(resp) # Print on screen the response 

	vidID = resp['items'][0]['id']['videoId']
	
	#print(vidID)

	# What does it do? This save on disk the last videoID so if the id read by the new json update is diferent from what is saved on file open the browser if not no
	video_exists = False
	with open('videoid.json', 'r') as json_file:
		data = json.load(json_file) 
		if data['videoId'] != vidID:
			driver = webdriver.Safari()	# .Chrome() seems to have a driver problem due to newer Chrome version
			# To work on Safari instead is necessary allow Remote Automation in Develop menu bars
			driver.get(base_video_url + vidID)
			video_exists = True
		if data['videoId'] == vidID:
			print("Youtube video already view")
	
	if video_exists:
		with open('videoid.json', 'w') as json_file:
			data = {'videoId' : vidID}
			json.dump(data, json_file)

try:
	while True:
		look_for_new_video()
		time.sleep(300)
except KeyboardInterrupt:
	print('stopping...')