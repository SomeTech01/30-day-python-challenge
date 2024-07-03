''' set.update(['mulit','items','here']) '''
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
print(type(fruits))
print(fruits)
print(type(vegetables))
print(vegetables)

fruits.update(vegetables)
print(fruits,' is the updated set')