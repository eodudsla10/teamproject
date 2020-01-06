import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup
import re
import datetime

# 부동산 내용
def crawler():
    for page in range(3):
        raw = requests.get('https://rent.heykorean.com/web/us/property/list?cp=' + str(page), headers={'User-Agent': 'Mozilla/5.0'}).text
        html = BeautifulSoup(raw, 'html.parser')
        articles = html.select('.title > div', class_='title-text')
    for article in articles:
        journal = article.select_one('div > a')
        if journal == None:
            print("")
        else:
            print(journal.text)
crawler()


# 카테고리
def category():
    go = urllib.request.urlopen(url='https://rent.heykorean.com/web/us/property/list')
    source = go.read()
    go.close()
    soup = BeautifulSoup(source, 'html.parser')
    articles = soup.select('div.module_content > ul > li')
    for article in articles:
        category = article.select_one('a').text
        print(category)

category()
#find_title = soup.select("#content > div.section_headline > ul > li > dl > dt > a")

#올린날짜
def date():
    for page in range(3):
        raw = requests.get('https://rent.heykorean.com/web/us/property/list?cp=' + str(page), headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(raw, 'html.parser')
        articles = html.select('table.rent-list-table > tbody > tr')
        for article in articles:
            journal2 = article.select_one("td.date center")
            print(journal2)
date()