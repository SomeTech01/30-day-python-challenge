''' var.startswith(str) check if the var starts with the specific str'''
print('startswith(): Checks if String Starts with the Specified String')
print('var.startswith(specific str)')
challenge = 'thirty days of python'
print(challenge)
print('print(challenge.startswith(\'thirty\'))')
print(challenge.startswith('thirty')) # True
print()
challenge = '30 days of python'
print(challenge)
print('print(challenge.startswith(\'thirty\'))')
print(challenge.startswith('thirty')) # False