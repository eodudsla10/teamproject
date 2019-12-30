import requests
from bs4 import BeautifulSoup
URL = "https://www.naver.com/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

finance_html = soup.select('div.area_links')
print(finance_html)