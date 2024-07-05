'''print(list[index]) to check what is in the specified index of the list
check for what item is in the index'''
print('Using positives for indexing. list[0 and so on]')
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]


'''Negative indexing'''
print()
print('Using negatives for indexing. list[-1 and so on]')
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
