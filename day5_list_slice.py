'''list[indexRange1:indexRange2]
list[indexRange1:indexRange2:increment]'''
"""positive slicing of list"""
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
print(all_fruits)
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(all_fruits)
orange_and_mango = fruits[1:3] # it does not include the first index
print(orange_and_mango)
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
print(orange_and_lemon)
print()
'''negative slicing of list'''
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
print(all_fruits)
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
print(orange_and_mango)
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
print(orange_mango_lemon)
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
print(reverse_fruits)

