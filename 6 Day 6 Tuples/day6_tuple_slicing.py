''' tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3 '''

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
print(fruits)
print(f'using tuple[0:4] or tuple[0:] returns everything like: {all_fruits}')
print(f'tuple[1:3] returns the item at index 1 and 2. Index 3 is where the count ends but wil not be returned.\n{orange_mango}')
print(f'tuple[1:] includes index and everything else: {orange_to_the_rest}')
print()
''' tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)'''

print('Using negatives to slice:')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
print(fruits)
print(f'tuple[-4:] returns everything:{all_fruits}')
print(f'tuple[-3:-1] excludes the first and last index: {orange_mango}')
print(f'tuple[-3:] excludes the first index: {orange_to_the_rest}')