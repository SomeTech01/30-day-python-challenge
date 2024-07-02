'''list.pop() removes the last item; list.pop(specific index) removes the item in the specific index '''
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print('remove the last item')
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']
print('remove the first index')
fruits.pop(0)
print(fruits)       # ['orange', 'mango']