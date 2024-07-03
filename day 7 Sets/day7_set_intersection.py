''' st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'} returns a set of items which are in both the sets.'''

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers)
print(even_numbers)
whole_numbers = whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(whole_numbers,'are the common items for both sets')
print()
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python)
print(dragon)
python = python.intersection(dragon)     # {'o', 'n'}
print(python,'are the common items for these')