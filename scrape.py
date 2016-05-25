from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://movie.douban.com/")
soup = BeautifulSoup(html, 'html.pa')
print(soup.text)