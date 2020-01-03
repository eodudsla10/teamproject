import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup
import re




for page in range(3):
    raw = requests.get('https://rent.heykorean.com/web/us/property/list?cp=' + str(page), headers={'User-Agent': 'Mozilla/5.0'}).text
    html = BeautifulSoup(raw, 'html.parser')
    articles = html.select('.title > div')
    for article in articles:
        journal = article.select_one('a').text
        #title = article.select_one('span.price').text
        print(journal)



#AttributeError: 'NoneType' object has no attribute 'text' 뭘 의미하는지??


def GetProductImformationList():
        for page in range(3):
            raw = requests.get('https://rent.heykorean.com/web/us/property/list?cp=' + str(page), headers={'User-Agent': 'Mozilla/5.0'}).text
            html = BeautifulSoup(raw, 'html.parser')
            articles = html.select(".rent-list-table> tbody> tr> .title > div")

        for article in articles:
            journal = article.select_one('a')#.text
             #title = article.select_one('.date center')#.text                 
            #print(journal)




