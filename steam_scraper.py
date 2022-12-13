from bs4 import BeautifulSoup
import requests

URL = 'https://steamcharts.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

top = soup.find(id = 'top-games')

games = top.find_all(class_ = 'game-name')

names = []

for i in range(0, len(games)):
    names.append(games[i].find('a'))

print(names)