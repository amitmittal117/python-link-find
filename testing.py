import bs4
import re
import urllib.request as uReq
from bs4 import BeautifulSoup as soup


def retriever_soup(my_url):
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	return (page_soup)

url = "http://dl.upload8.net/Serial/11.22.63" 

size= uReq.urlopen(url).headers['Content-Length']
print ((str(size)))