import bs4
import re
import requests
from urllib.request import urlopen as uReq
import urllib.request as req
from bs4 import BeautifulSoup as soup

def regression(any_url):
	print (any_url)
	uClient = uReq(any_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser").findAll("a")
	for i in page_soup:
		new_temp = (any_url+i.get("href"))
		if new_temp[-1] == "/" and new_temp[-2] != "." and new_temp[-3] != ".":
			regression(new_temp)
			# print("NEXT")
		else:
			print(new_temp)



url = "http://dl.upload8.net/"

regression(url)