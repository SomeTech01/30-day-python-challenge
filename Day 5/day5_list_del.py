'''del list[index] to remove specific item; del list remove the list completely '''
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
print(fruits)
print('delete index 0')
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
print('delete index 1')
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
print('delete index between 1:3')
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
print('delete the whole list and errors out')
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined