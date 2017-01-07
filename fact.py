#Program that counts factorials plus logging
import logging

logging.basicConfig("""filename = 'myProgramLog.txt',""" level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def fact(number):
    if number == 1:
        return number
    else:
        return (number * fact(number - 1))

def fact2(number):
    logging.debug('Start of factorial(%s)' % (number))
    total = 1
    for i in range(1, number + 1):
        total *= i
        logging.critical('i is {}, total is {}'.format(i, total))
    logging.debug('Return value is {}'.format(total))        
    return total

print(fact(7))

print(fact2(7))

logging.debug('End of program')
