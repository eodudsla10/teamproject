import urllib.request
import requests
from bs4 import BeautifulSoup
import re

maximum = 0
page = 1

URL = 'https://rent.heykorean.com/web/us/property/list?cp=1'
response = requests.get(URL)
source = response.text
soup = BeautifulSoup(source, 'html.parser')

while 1:
	page_list = soup.findAll("a", {"class": "NP=r:" + str(page)})
	if not page_list:
		maximum = page - 1
		break
	page = page + 1
print("총 " + str(maximum) + " 개의 페이지가 확인 됬습니다.")

whole_source = ""
for page_number in range(1, maximum+1):
	URL = 'https://rent.heykorean.com/web/us/property/list?cp=1' + str(page_number)
	response = requests.get(URL)
	whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')
find_title = soup.select("#content > div.section_headline > ul > li > dl > dt > a")

for title in find_title:
	print(title.text)