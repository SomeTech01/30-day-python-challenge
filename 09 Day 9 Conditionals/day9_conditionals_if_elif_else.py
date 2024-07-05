''' Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, 

if condition:
    this part of code runs for True conditions'''

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
print()
''' if condition:
    this part of code runs for true conditions
else:
    this part of code runs for false conditions'''

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
print()
'''if condition:
    code
elif condition:
    code
else:
    code '''

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')