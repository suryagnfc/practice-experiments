import os

print (os.getcwd())
MadlibsFile = open(os.path.join(os.getcwd(),'TestFiles','MadLibs.txt'))

MadlibsFileContent = MadlibsFile.readlines()
TextAfterModification= []
for line in MadlibsFileContent:
    lineList= line.split(' ')
    for item in lineList:
        if item == 'ADJECTIVE':
            adjectiveIndex = line.index("ADJECTIVE")
            print('Enter an ADJECTIVE')
            replaceADJECTIVE = input()
            line = line[0:adjectiveIndex] + replaceADJECTIVE + line[adjectiveIndex+9:]
            
        if item == 'NOUN':
            NOUNIndex = line.index('NOUN')
            print('Enter an NOUN')
            replaceNOUN = input()
            line= line[0:NOUNIndex] + replaceNOUN + line[NOUNIndex+4:]
        if item == 'VERB' or item == 'VERB.' or item == '.VERB':
            verbIndex = line.index('VERB')
            print('Enter an VERB' + str(verbIndex))
            replaceVERB = input()
            line =line[0:verbIndex] + replaceVERB + line[verbIndex+4:]
            
    TextAfterModification.append(line)
    print(TextAfterModification)
    
MadlibsFile.close()
        
MadlibsFile = open(os.path.join(os.getcwd(),'TestFiles','MadLibs.txt'),'w')
MadlibsFile.write(''.join(TextAfterModification))
MadlibsFile.close()
