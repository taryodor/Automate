#Program to store traceback info to the file

import traceback

try:
    raise Exception
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.write('\n')
    errorFile.close()
    print('The traceback info was writen into error_log.txt')
    
