''''set.add('item') added at the end of the set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) '''

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
fruits.add('lime')
print(fruits)

print('Using update()')
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits)
print(vegetables)
fruits.update(vegetables)
print(fruits,'is the updated set') # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}