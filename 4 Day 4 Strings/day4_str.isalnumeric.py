'''var.isalnum() check if the content of the var is alphanumeric'''
challenge = 'ThirtyDaysPython'
print('Checking if the following are alphanumeric')
print('use var.alnum()')
print(challenge)
print(challenge.isalnum()) # True
print()
challenge = '30DaysPython'
print(challenge)
print(challenge.isalnum()) # True
print()
challenge = 'thirty days of python'
print('Space is not alpha numeric therefore:')
print(challenge)
print(challenge.isalnum()) # False, space is not an alphanumeric character
print()
challenge = 'thirty days of python 2019'
print(challenge)
print(challenge.isalnum()) # False