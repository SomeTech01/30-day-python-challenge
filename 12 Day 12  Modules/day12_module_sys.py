''' sys module provides functions and variables used to manipulate different parts of the Python runtime environment'''

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
## if this script runs first arg goes to the first {} 
## 0 i the script itself, 1 is the first arg provided, and so on

''' # to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version'''
