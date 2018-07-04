import bs4
import re
import requests
from urllib.request import urlopen as uReq

import urllib.request as req
from bs4 import BeautifulSoup as soup

def retriever_soup(my_url):
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	return (page_soup)


my_url = 'http://dl.upload8.net/Serial/'

a_href = retriever_soup(my_url).findAll("a")
total = 0
for i in a_href:
	new_link = my_url+i.get('href')
	inner_data = retriever_soup(new_link).findAll("a")
	for j in inner_data:
		main_link = new_link+j.get('href')
		r = requests.get(main_link)
		print(r.status_code)
		if r.status_code == 400:
			print(str(main_link)+ " ERROR")
		else:
			size= req.urlopen(main_link).headers['Content-Length']
			print (main_link)
			print (size)
	# 	size= req.urlopen(main_link).headers['Content-Length']
	# 	size = int(size)/(1024*1024)
	# 	total = total + size
	# 	print (main_link+ " : " + str(size) + " MB")
	# print (str(total)+ " MB")