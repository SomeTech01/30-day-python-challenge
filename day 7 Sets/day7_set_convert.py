''''
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered'''
fruits_list = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits_set = set(fruits_list) # {'mango', 'lemon', 'banana', 'orange'} no duplicates
print(type(fruits_list))
print(fruits_list)
print(type(fruits_set))
print(fruits_set)
