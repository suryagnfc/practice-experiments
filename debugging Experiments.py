#raise exceptions

def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('Symbol must be a single character string.')
    if width <=2:
        raise Exception('Width must be greater than 2.')
    if height <=2:
        raise Exception('height must be greater than 2.')

    print (symbol*width)
    for i in range(height-2):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O',20,5), ('x',1,3), ('ZZ', 3,3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print ('An exception happened: '+ str(err))

        
#traceback as string in file
import traceback


try:
    raise Exception ('This is the error message.')
except:
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')



#Assertion
#uncomment below assert statements to get program running else it will crash.
    
podBayDoorStatus='open'
#assert podBayDoorStatus == 'open', 'The pod door need to be "open".'
podBayDoorStatus ='I\'m sorry, Dave. I\'m afraid I can\'t do that.'
#assert podBayDoorStatus == 'open', 'The pod door need to be "open".'



#logging module.

import logging
#to disable logging logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('start of program')

def factorial(n):
    logging.debug('start of factorial(%s)'%(n))
    total =1
    for i in range(1,n+1):
        total =total* i
        logging.debug('i is' + str(i) +', total is' + str(total))
    logging.debug('End of factorial(%s)' %(n))
    return total

print(factorial(5))
logging.debug('End of Program')

