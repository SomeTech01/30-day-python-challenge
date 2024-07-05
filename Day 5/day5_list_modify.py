'''modify list by using list[specific index] = 'item' '''
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print('adds avocado on the first index [0]')
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
print('adds apple to the second index [1]')
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
print('adds lime to the end of the list using var[-1] = "lime"')
last_index = len(fruits) - 1 ## last_index = 4-1
fruits[last_index] = 'lime' ## fruits[3] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
