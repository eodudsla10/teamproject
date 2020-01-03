import urllib.request
import requests
from bs4 import BeautifulSoup
import re

maximum = 0
page = 1

URL = 'https://rent.heykorean.com/web/us/property/list?cp'
response = requests.get(URL)
source = response.text
soup = BeautifulSoup(source, 'html.parser')

while 1:
	page_list = soup.findAll("a", class_='page-link', href='/web/us/property/list?cp=' + str(page))
	if not page_list:
		maximum = page - 1
		break
	page = page + 1
print("총 " + str(maximum) + " 개의 페이지가 확인 됬습니다.")

whole_source = ""
for page_number in range(1, maximum+1):
	URL = 'https://rent.heykorean.com/web/us/property/list?cp=' + str(page_number)
	response = requests.get(URL)
	whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')
find_title = soup.select('div', class_='title-text')
#find_title = soup.select("#content > div.section_headline > ul > li > dl > dt > a")
#find_title = soup.select('td', class_='title')
#find_title = soup.select('td', class_='image center')
for title in find_title:
	print(title.text)