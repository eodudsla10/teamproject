from bs4 import BeautifulSoup
import requests
res = requests.get('https://www.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
link_title = soup.select('span.ah_k')
# for num in range(len(link_title)):
print(link_title.prettify())
  