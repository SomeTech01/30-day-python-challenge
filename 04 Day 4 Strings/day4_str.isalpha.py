'''var.islapha() check if the str are alpahbets'''
print('Checking if all the str are alphabets')
challenge = 'ThirtyDaysPython'
print(challenge)
print(challenge.isalpha()) # True
print()
challenge = 'thirty days of python'
print('Space is not an alphabet therefore:')
print(challenge)
print(challenge.isalpha()) # False, space is once again excluded
print()
print('Numbers are not alphabet xD')
num = '123'
print(num)
print(num.isalpha())      # False