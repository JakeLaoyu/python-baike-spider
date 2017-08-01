import urllib.request
from bs4 import BeautifulSoup


url = "https://i.jakeyu.top"

response1 = urllib.request.urlopen(url)
# print(response1.getcode())

soup = BeautifulSoup(response1.read(), 'html.parser', from_encoding="urf-8")

# print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())
