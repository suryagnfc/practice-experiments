import os
import random
import re

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

players =['x','o']
turn =''
gameNumber=0

def gameStatus():
    if((theBoard['top-L']=='x' and theBoard['top-M']=='x' and theBoard['top-R']=='x') or
       (theBoard['top-L']=='x' and theBoard['mid-M']=='x' and theBoard['low-R']=='x') or
       (theBoard['top-L']=='x' and theBoard['mid-L']=='x' and theBoard['low-L']=='x') or
       (theBoard['mid-L']=='x' and theBoard['mid-M']=='x' and theBoard['mid-R']=='x') or
       (theBoard['low-L']=='x' and theBoard['low-M']=='x' and theBoard['low-R']=='x') or
       (theBoard['top-M']=='x' and theBoard['mid-M']=='x' and theBoard['low-M']=='x') or
       (theBoard['top-R']=='x' and theBoard['mid-R']=='x' and theBoard['low-R']=='x') or
       (theBoard['top-R']=='x' and theBoard['mid-M']=='x' and theBoard['low-L']=='x')):
        return 'x'

    if((theBoard['top-L']=='o' and theBoard['top-M']=='o' and theBoard['top-R']=='o') or
       (theBoard['top-L']=='o' and theBoard['mid-M']=='o' and theBoard['low-R']=='o') or
       (theBoard['top-L']=='o' and theBoard['mid-L']=='o' and theBoard['low-L']=='o') or
       (theBoard['mid-L']=='o' and theBoard['mid-M']=='o' and theBoard['mid-R']=='o') or
       (theBoard['low-L']=='o' and theBoard['low-M']=='o' and theBoard['low-R']=='o') or
       (theBoard['top-M']=='o' and theBoard['mid-M']=='o' and theBoard['low-M']=='o') or
       (theBoard['top-R']=='o' and theBoard['mid-R']=='o' and theBoard['low-R']=='o') or
       (theBoard['top-R']=='o' and theBoard['mid-M']=='o' and theBoard['low-L']=='o')):
        return 'o'    

    return 1

#function to display the board from dictionary.
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#does a toss and returns whose chance is to start.
def toss():
    global players
    return(random.randint(0,1))

#gameHandle() handles the main game flow. - displays tictactoe after every chance.
#call the function to check winner after every chance
#prints the chance and other messages
#call the function to save the winner detail along with screenshot to file.

def gameHandle():
    global turn
    chance =0
    game_status=1
    while game_status!=0:
        print()
        print('Where do you want to put ' + turn)
        place = input()
        if place not in theBoard.keys():
            print('Enter correct place')
        else:
            if(theBoard[place] == ' '):
                theBoard[place]=turn
                if (turn=='x'):
                    turn = 'o'
                else:
                    turn = 'x'
            else:
                print('Place already filled. Choose another position.')
        game_status = gameStatus()
        if (game_status=='x'):
            print('X won the game!!!!')
            printBoard(theBoard)
            saveWinner('X won the Game.')
            chanceScreenshots('','X won the game!!! \n',chance,theBoard)
            break
        elif (game_status=='o'):
            print('O won the game!!!!')
            printBoard(theBoard)
            saveWinner('O won the Game.')
            chanceScreenshots('','O won the game!!! \n',chance,theBoard)
            break
    
        printBoard(theBoard)
        chance= chance+1
        saveWinner()
        chanceScreenshots(turn,'',chance,theBoard)

def getGameNumber():
    global gameNumber
#checking if the directory is present or not. If not then create a directory from the current working directory
    if (os.path.exists(os.path.join(os.getcwd(),'TestFiles')) != True):
        os.makedirs(os.path.join(os.getcwd(),'TestFiles'))
#getting the path as Text by using Join
    path = os.path.join(os.getcwd(),'TestFiles')
#adding the name of file to path that will be refered to same gave summary details.    
    fileName = path + '\\'+ 'TicTacToe.txt'
#opening the file in read mode
    fileObj = open(fileName, 'r')
#Reading all the content at one go.
    existingFileContent = fileObj.read()
#creating a regular expression to get the game number detail from the file.
    gameRegEx= re.compile(r'Game \d')
#finding all the combination found from the file for the regular expression.
    mo = gameRegEx.findall(existingFileContent)
#if there is atleast one game number then go to else part else set the game as 1    
    if len(mo) >=1:
        lastGame = mo[len(mo)-1]
#get the last text combination found from the file by using regular expression.
        lastGameNumber = lastGame.split(' ')
#convert the text1 to int 1 and then increase by 1(for this game)
        gameNumber = (int(lastGameNumber[1])) +1
    else:
        gameNumber=1

    #fileObj.write('X won')
    fileObj.close()

def chanceScreenshots(turn, text, chance,theboard):
    
    if (os.path.exists(os.path.join(os.getcwd(),'TestFiles')) != True):
        os.makedirs(os.path.join(os.getcwd(),'TestFiles'))

    path = os.path.join(os.getcwd(),'TestFiles')
    
    fileName = path + '\\'+ 'TicTacToe_screenshots.txt'
    
    
    fileObj = open(fileName, 'a')
    if (chance ==1):
        fileObj.write('\n========================Game No %d screenshot==========================='%(gameNumber))
    fileObj.write('\n')
    if (turn!=''):
        fileObj.write(str(turn) + ' turn - \n')
    if (text!=''):
        fileObj.write(str(text))
    fileObj.write(theboard['top-L'] + '|' + theboard['top-M'] + '|' + theboard['top-R'] + '\n')
    fileObj.write('-+-+-\n')
    fileObj.write(theboard['mid-L'] + '|' + theboard['mid-M'] + '|' + theboard['mid-R']+'\n')
    fileObj.write('-+-+-\n')
    fileObj.write(theboard['low-L'] + '|' + theboard['low-M'] + '|' + theboard['low-R']+'\n')
    fileObj.close()
    

def saveWinner(winnerDetail):
    global gameNumber
    if (os.path.exists(os.path.join(os.getcwd(),'TestFiles')) != True):
        os.makedirs(os.path.join(os.getcwd(),'TestFiles'))
    path = os.path.join(os.getcwd(),'TestFiles')
    #print(path)
    fileName = path + '\\'+ 'TicTacToe.txt'
    #print(fileName)
    fileObj = open(fileName, 'a')
    fileObj.write('\n========Game %d ========'%(gameNumber))
    fileObj.write('\n'+winnerDetail + '\n open screenshow to get the screen shot of game\n')
    fileObj.close()


def welcome():
    global turn
    global gameNumber
    print('Welcome to Game no: %d' %(gameNumber))
    print('Lets play the game!')
    print('Doing Toss between player x turn and player o')
    print()
    turn =players[toss()]
    print(turn + ' won the toss!')
    printBoard(theBoard)

getGameNumber()
welcome()
gameHandle()

