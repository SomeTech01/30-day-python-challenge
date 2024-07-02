'''list.sort() ascending order
list.sort(reverse=True) descending order '''

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print('Print out sorted list using list.sort():')
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
print('Print out reversely sorted list  using list.sort(reverse=True):')
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
print()
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages)
print('Print out sorted list using list.sort():')
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
print('Print out reversely sorted list:')
ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
print()
''' using sorted
sorted(list) ascending order
sorted(list, reverse=True) descending order'''
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print('Print out sorted list using sorted():')
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Print out sorted list using sorted(list,reverse=True):')
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
