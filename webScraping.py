import webbrowser, sys
import requests, logging
import bs4

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')
""" putting below open commands as comment 
webbrowser.open('http://maps.google.com/')
logging.info('After First mapps google.com')

webbrowser.open('http://inventwithpython.com/')
logging.info('After inventwithPython.com')

webbrowser.open('http://maps.google.com/')
logging.info('After second mapps google.com')
"""
#getting the automate the boring stuff.com HTML page
res=requests.get('http://automatetheboringstuff.com/')
print(res.status_code)
try:
    res.raise_for_status()
except Exception as Exc:
    print('there was problem: %s'%(Exc))
    
#print(res.text)





#getting the romeo and juliet .txt file from site.

res=requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
try:
    res.raise_for_status()
except Exception as Exc:
    print('there was problem: %s'%(Exc))
#playFile = open('romeoAndjuliet.html','wb')
playFile = open('romeoAndjuliet.txt','wb')

for chunk in res.iter_content(100000):
    #print (chunk)
    playFile.write(chunk)
    #sprint('Got 100000 chunk, Press anykey to continue!.')
    #input()

playFile.close()







# getting the Facebook site.
res=requests.get('http://facebook.com/')
print(res.status_code)
try:
    res.raise_for_status()
except Exception as Exc:
    print('there was problem: %s'%(Exc))
    
#print(res.text)





#parsing with Beautiful soap.
sitehtml =open('example.html').read()
print(sitehtml)
exampleSoup = bs4.BeautifulSoup(sitehtml)
elements = exampleSoup.select('p')
print(len(elements))
print(elements)
