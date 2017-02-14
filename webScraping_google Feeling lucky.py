import requests, webbrowser, bs4

print('enter the test to search from google')
textToSearch = input()
print('Googling.....')

res = requests.get('http://google.com/search?q='+textToSearch)

try:
    res.raise_for_status()
except Exception as exc:
    print('Exception was caught while getting search result from Google. %s' %(exc))

SearchResult = bs4.BeautifulSoup(res.text)
classElements = SearchResult.select('.r a')
print(len(classElements))
for i in range(len(classElements)):
    print('--------------Opening======================')
    print(classElements[i])
    webbrowser.open('http://google.com'+classElements[i].get('href'))
    print('------------------------------------=============================')
    
