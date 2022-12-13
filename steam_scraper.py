from bs4 import BeautifulSoup
import requests

URL = 'https://steamcharts.com/'

def get_top():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    top = soup.find(id = 'top-games')
    games = top.find_all(class_ = 'game-name')
    
    names = []
    
    for i in range(0, len(games)):
        names.append(games[i].find('a'))
    
    return names

def get_data(game):

    url = f"{URL}search/?q= {game}"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    games = soup.find_all('td')
    
    names = []

    for i in range(0, len(games)):
        names.append(games[i].find('a'))

    return names

def clean(names):

    for i in range(0,len(names)):
        names[i] = str(names[i])

    removes = []
    
    for a in range(0,len(names)):
        name = str(names[a])
        for i in range(0,len(name)):
            if name[i:i+1] == '<':
                remove = ''
                for j in range(i,len(name)):
                    remove = remove + str(name)[j:j+1]
                    if name[j:j+1] == '>':
                        break
                removes.append(remove)
                remove = ''
    
    namesTemp = []
    
    for a in range(0, len(names)):
        
        name = str(names[a])
        
        for i in range(a,len(removes)):
            name = name.replace(removes[i], '')
            
        name = name.replace('\n', '')
        name = name.replace('\t', '')
        namesTemp.append(name)
    
    namesC = []

    for name in namesTemp:
        namesC.append(name)
        
    return namesC

def pair(names, players):
    pairs = {}
    
    for i in range(0,len(names)):
        pairs.update({names[i]:players[i]})
    
    return pairs

print(clean(get_top()))