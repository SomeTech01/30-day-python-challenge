'''var.find('str') to look for the first occurence of the str
var.rfind('str') to look for the last occurence of the str'''
challenge = 'thirty days of python'
print(challenge)
print('Find the index of the first occurence of a character')
print('print(challenge.find(\'y\)) ')
print(challenge.find('y'))  # 5
print('print(challenge.find(\'th\'))')
print(challenge.find('th')) # 0
print()
print('Using rfind for the last occurence of the character')
print('print(challenge.rfind(\'y\'))')
print(challenge.rfind('y'))
print('print(challenge.rfind(\'th\'))')  
print(challenge.rfind('th'))