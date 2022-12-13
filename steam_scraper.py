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

namesC = names[:]
length = len(namesC)

def find_clean(names):
    
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
    
    return removes

def clean(names):
    
    namesTemp = []
    
    removes = find_clean(names)
    
    print(removes)
    
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