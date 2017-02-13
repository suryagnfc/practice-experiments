import os

print (os.getcwd())
MadlibsFile = open(os.path.join(os.getcwd(),'TestFiles','MadLibs.txt'))

MadlibsFileContent = MadlibsFile.readlines()
TextAfterModification= []
for line in MadlibsFileContent:
    lineList= line.split(' ')
    for item in lineList:
        if item == 'ADJECTIVE':
            adjectiveIndex = lineList.index('ADJECTIVE')
            print('Enter an ADJECTIVE')
            replaceADJECTIVE = input()
            lineList.remove('ADJECTIVE')
            lineList.insert(adjectiveIndex,replaceADJECTIVE)
        if item == 'NOUN':
            NOUNIndex = lineList.index('NOUN')
            print('Enter an NOUN')
            replaceNOUN = input()
            lineList.remove('NOUN')
            lineList.insert(NOUNIndex,replaceNOUN)
        if item == 'VERB' or item == 'VERB.' or item == '.VERB':
            verbIndex = lineList.index('VERB.')
            print('Enter an VERB')
            replaceVERB = input()
            lineList.remove('VERB.')
            lineList.insert(verbIndex,replaceVERB+'.')
        
    StringLine= ' '.join(lineList)
    TextAfterModification.append(StringLine)
    print(TextAfterModification)
    


MadlibsFile.close()
        
