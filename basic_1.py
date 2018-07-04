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

def regression (any_url):
	
	for i in retriever_soup(my_url).find("a"):
		if ((my_url+i.get('href')[-1])=="/"):
				regression(my_url+i.get('href'))
		else:
			return(my_url+i.get('href'))


my_url = 'http://dl.upload8.net/'

got_yaa = regression(my_url)

for every_link in got_yaa:
	print (every_link)


# for i in retriever_soup(my_url).findAll("a"):
# 	if (my_url+i.get('href')[-1]=="/"):
# 		a_href_next = retriever_soup(my_url).findAll("a")

# 		for j in a_href_next:
# 			main_link = my_url+i.get('href')
# 			print(main_link)

