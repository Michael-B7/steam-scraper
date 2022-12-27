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
        
    players = top.find_all(class_ = 'num')
    
    playersC = players[:]
    
    for i in range(0,len(players)):
        if not i % 3 == 0:
            playersC.remove(players[i])
    
    players = []
    players = playersC[:]
    
    data = []
    
    for i in range(0,len(names)):
        data.append(names[i])
        data.append(players[i])
    
    return data

def get_data(game):

    url = f"{URL}search/?q= {game}"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    games = soup.find_all('td')
    
    names = []

    for i in range(0, len(games)):
        names.append(games[i].find('a'))

    return names

def clean(data):

    for i in range(0,len(data)):
        data[i] = str(data[i])

    removes = []
    
    for a in range(0,len(data)):
        val = str(data[a])
        for i in range(0,len(val)):
            if val[i:i+1] == '<':
                remove = ''
                for j in range(i,len(val)):
                    remove = remove + str(val)[j:j+1]
                    if val[j:j+1] == '>':
                        break
                removes.append(remove)
                remove = ''
    
    dataTemp = []
    
    for a in range(0, len(data)):
        
        val = str(data[a])
        
        for i in range(a,len(removes)):
            val = val.replace(removes[i], '')
            
        val = val.replace('\n', '')
        val = val.replace('\t', '')
        dataTemp.append(val)
    
    data = []

    for val in dataTemp:
        data.append(val)
        
    return data

def pair(data):
    
    pairs = {}
    
    for i in range(0,len(data)):
        if i % 2 == 0:
            pairs.update({data[i]:data[i+1]})
    
    data1.append(names)
    data1.append(players)
    
    return data1

print(separate(clean(get_top())))