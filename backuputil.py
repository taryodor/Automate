#Nice little program to backup all files with specific
#extension
import os, shutil

for folderName, subFolders, fileNames in os.walk('./'):
    for file in fileNames:
        if file.endswith('.py'):
            #shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
            print(folderName, file)


