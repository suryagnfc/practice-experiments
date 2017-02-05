import os

if (os.path.exists(os.path.join(os.getcwd(),'TestFiles')) != True):
    os.makedirs(os.path.join(os.getcwd(),'TestFiles'))

path = os.path.join(os.getcwd(),'TestFiles')
print(path)
fileName = path + '\\'+ 'TicTacToe.txt'
print(fileName)
fileObj = open(fileName, 'w')
fileObj.write('X won')
fileObj.close()
