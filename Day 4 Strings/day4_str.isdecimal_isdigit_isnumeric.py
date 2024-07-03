'''var.isdecimal() check if the content of a var is a decimal
var.isdigit() Return true if all characters in the string are digits and there is at least one character, false otherwise
var.isnumeric() Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise'''
print('isdecimal(): Checks if all characters in a string are decimal (0-9)')
print('var.isdecimal')
challenge = 'thirty days of python'
print(f'{challenge} is composed of alphabets')
print(challenge.isdecimal())  # False
challenge = '123'
print(f'{challenge} are numbers')
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(f'{challenge} is an exponent')
print(challenge.isdigit())   # False
challenge = '12 3'
print(f'{challenge} has a space')
print(challenge.isdecimal())  # False, space not allowed
print()
print('isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)')
print('var.isdigit()')
print(f'{challenge} is composed of alphabets')
print(challenge.isdigit()) # False
challenge = '30'
print(f'{challenge} is a number')
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(f'{challenge} is a number')
print(challenge.isdigit())   # True
print()
print('isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)')
print('var.isnumeric()')
num = '10'
print(f'{num} is a number')
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(f'{num} is a number')
print(num.isnumeric()) # True
num = '10.5'
print(f'{num} is a float therefore it is:')
print(num.isnumeric()) # False