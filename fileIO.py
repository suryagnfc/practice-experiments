import os
import re

if (os.path.exists(os.path.join(os.getcwd(),'TestFiles')) != True):
    os.makedirs(os.path.join(os.getcwd(),'TestFiles'))

path = os.path.join(os.getcwd(),'TestFiles')
print(path)
fileName = path + '\\'+ 'test_game number.txt'
print(fileName)
fileObj = open(fileName, 'r')
existingFileContent = fileObj.read()

gameRegEx= re.compile(r'game \d')
mo = gameRegEx.findall(existingFileContent)
lastGame = mo[len(mo)-1]

lastGameNumber = lastGame.split(' ')
print(int(lastGameNumber[1]))
print(mo[len(mo)-1])

#fileObj.write('X won')
fileObj.close()
