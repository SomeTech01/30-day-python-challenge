'''
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]'''

print('Using positives for the tuple')
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(fruits)
print(f'tuple[0] has the item {first_fruit}')
print(f'tuple[1] has the item {second_fruit}')
print(f'The last index number of the tuple is {last_index}')
print(f'{last_fruit} is the item on this index')

print()
'''
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3] '''
print('Using negatives for the tuple')
print(fruits)
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(f'tuple[-4] will return {first_fruit}')
print(f'tuple[-3] returns {second_fruit}')
print(f'{last_fruit} is returned when you use tuple[-1]')