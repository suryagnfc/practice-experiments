
listInList = ['a', 'b', 'c', 'd']

print(listInList[0] + '\n')

for index in range(len(listInList)):
    print (listInList[index])

print("reverse ->")

for index in range(len(listInList)-1, -1 , -1):
    print (listInList[index])

print("direct values ->")

for index in (listInList):
    print (index)

print ("index of direct values ->")

for index in (listInList):
    print (listInList.index(index))


listInList = ['a', 'b', [1,2,3,4,5], 'd']

print("list inside list")

for index in (listInList):
    print (index)

#print(' '+ str(type(listInList)) +' ' + str(type(listInList) == list))
print ("")
#print ("Trying recurssion to get list inside list")

def listInsideList (list):
    #print('1 ->')
    #print(list)
    for index in (list):
       # print('-' + str(type(index)) + '- ' + str(str(type(index)) == "<class 'list'>"))
        
        if (str(str(type(index)) == "<class 'list'>") == "True"):
           # print('inside if condition')
            listInsideList (index)
        else:
            print (index)
    return 0       
listInsideList (listInList)

