'''var.isidentifier() check if is a valid var name
var.islower()
var.isupper()'''
print('isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name')
print('var.isindetifier()')
challenge = '30DaysOfPython'
print(challenge)
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge)
print(challenge.isidentifier()) # True
print()
print('islower(): Checks if all alphabet characters in the string are lowercase')
print('var.islower()')
challenge = 'thirty days of python'
print(challenge)
print(challenge.islower()) # True
print(challenge)
challenge = 'Thirty days of python'
print(challenge.islower()) # False
print()
print('isupper(): Checks if all alphabet characters in the string are uppercase')
print('var.isupper()')
challenge = 'thirty days of python'
print(challenge)
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge)
print(challenge.isupper()) # True