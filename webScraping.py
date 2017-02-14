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

elements = exampleSoup.select('#author')
print(len(elements))
print(elements[0])
print(elements[0].getText())
print(elements[0].attrs)

elements = exampleSoup.select('p')
print(len(elements))
print(elements[0])
print(elements[1])
print(elements[2])


#getting data from and element's attributes

spanElem = exampleSoup.select('span')[0] # when [0] is put at this position then the
#spanElem will be of type - <class 'bs4.element.Tag'>, and we can use the .get() function.
#but if we dont put [0] then the spanElem will be of type <class 'list'> and we
#wont be able to use .get() function
print(type(spanElem))
print(spanElem)
print(spanElem.get('id'))
