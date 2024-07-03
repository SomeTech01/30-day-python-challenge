''' var.split() splits the content of a var '''
print('split(): Splits the string, using given string or space as a separator')
print('var.split(separator)')
print()
challenge = 'thirty days of python'
print(challenge)
print('print(challenge.split())')
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
print()
challenge = 'thirty, days, of, python'
print(challenge)
print('print(challenge.split(\', \'))')
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']