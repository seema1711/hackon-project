#!/usr/bin/python36

# imported the requests library
import requests
file_url=input("Enter the URL of the file you want to download")

# URL of the file to be downloaded is defined as file_url
r= requests.get(file_url)

# send a HTTP request to the server and save 
# the HTTP response in a response object called r 

file_name=input("Enter the name of the file you want to download")
with open(file_name,"wb") as file:
	for chunk in r.iter_content(chunk_size=1024):
		# writing one chunk at a time to pdf file 
		if chunk: 
			file.write(chunk)
