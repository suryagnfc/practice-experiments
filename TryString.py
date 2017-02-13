str ='hello how are you. doing. you. you. you are doing ?'
listStr = list(str)

NewStr = str.split(' ')

"""
print(NewStr)
youIndex = NewStr.index('you')
print (youIndex)

NewStr.insert(youIndex,'No')
print (NewStr)

NewStr.remove('you')
print (NewStr)
"""

"""
str = str.replace("you","u")
print (str)
"""
youIndex = str.index("you")
str = str[0:youIndex] + input() + str[youIndex+3:]
print (str)

