'''' st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2 
gives you elements that are only in the first set and not in the second set
set1 - set2 = what ever remains is printed out '''
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
diffenrece = whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9} # These are found in the first set and not in the second set
difference1 = even_numbers.difference(whole_numbers) # bigger set goes first. This retuns set()
print(diffenrece)
print(difference1)
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))    # {'d', 'r', 'a', 'g'}

''''  st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
gives you elements that are unique to either set but not common to both.
(set1 - set 2) + (set2 - set1) = puts reaminder items for both then combines them  '''

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}