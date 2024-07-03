''''  st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
two sets do not have a common item or items we call them disjoint sets
check if there is no common items'''

odd_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
check_even = even_numbers.isdisjoint(odd_numbers) # True, because no common item
print(odd_numbers)
print(even_numbers)
print('isdisjoint checks if there is nothing in common between 2 sets. Nothing in common for these: ', check_even)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
check_pyhon = python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
print(python)
print(dragon)
print('This two sets has nothing in common:',check_pyhon)