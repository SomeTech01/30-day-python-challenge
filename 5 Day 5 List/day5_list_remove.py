'''list.remove(item) '''


fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
print(fruits)
print('remove banana')
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
print('remove lemon')
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
