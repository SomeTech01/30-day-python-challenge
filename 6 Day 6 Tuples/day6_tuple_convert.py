'''
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)'''

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits) ## converts fruits to list
fruits[0] = 'apple' ## insert apple at index 0
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits) ## converts the list back to tuple
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')