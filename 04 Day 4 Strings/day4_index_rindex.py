'''var = var[index]'''
print('Indexing using var= var[index number]')
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
print('Indexing using -1 and so on')
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

print()
print('Can also be coded as var.index[str to index]:')
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge)
print(print(f'the string I\'m looking for is {sub_string}'))
print('print(challenge.index(sub_string))')
print(challenge.index(sub_string))
print()
print('Using rindex to retrun the highest index of the str.')
rstring= 'th'
print(challenge)
print(f'the string I\'m looking for is {rstring}')
print('print(challenge.rindex(rstring))')
print(challenge.rindex(rstring)) 
