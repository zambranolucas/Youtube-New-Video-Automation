Open New Youtube Video Channel Python Automation

- This project open new video upload from a selected channelID

- Issue run out during test:
	- Error 403 access forbbidden, it seems due to the usage limits of request to API endpoint, I try to fix this problem at the beginning using a different User-Agent in the header of the request but then I understood that was an error of limits exceeded, by searching the entire request to API endpoint directly on browser 
	- To go throught this kind of problem create or delete a project on google console developer and enable youtube API v3 and create a new one key credential