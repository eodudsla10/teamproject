import urllib.request
import requests
from bs4 import BeautifulSoup
import re

# 부동산 올린 날짜
def GetProductDate(link):
    if link == 0:
        list_property = []
        for page in range(3):
            raw = requests.get('https://rent.heykorean.com/web/us/property/list?cp=' + str(page), headers={'User-Agent': 'Mozilla/5.0'}).text
            soup = BeautifulSoup(raw, 'html.parser')
            for all_range in soup.find_all('td', class_='date center'):
                list_property.append(str(all_range.text))
        return list_property
#print(GetProductDate(0))

# 부동산 내용
def GetProductContents(link):
    if link == 0:
        list_property = []
        for page in range(3):
            raw = requests.get('https://rent.heykorean.com/web/us/property/list?cp=' + str(page), headers={'User-Agent': 'Mozilla/5.0'}).text
            soup = BeautifulSoup(raw, 'html.parser')
            coment = soup.select('div.title-text > a[href]')
            for all_range in coment:
                list_property.append(all_range.text)

        return list_property
#print(GetProductContents(0))


# 카테고리
def GetProductCategory(link):
    if link == 0:
        list_property = []
        raw = requests.get('https://rent.heykorean.com/web/us/property/list').text
        soup = BeautifulSoup(raw, 'html.parser')
        coment = soup.select('div.sidebar_module > div.module_content > ul > li > a[href]')
        for all_range in coment:
            list_property.append(all_range.text)
        del list_property[:4]
        return list_property
#print(GetProductCategory(0))

# 페이지1 부동산 가격
def GetProductPrice(link):
    if link == 0:
        list_property = []
        for page in range(3):
            raw = requests.get('https://rent.heykorean.com/web/us/property/list?cp=' + str(page), headers={'User-Agent': 'Mozilla/5.0'}).text
            soup = BeautifulSoup(raw, 'html.parser')
            for all_range in soup.find_all('span', class_='price'):
                list_property.append(str(all_range.text))
        return list_property
#print(GetProductPrice(0))


