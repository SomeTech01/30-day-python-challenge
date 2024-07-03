'''Exercises: Level 2

Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_staff_lt list
Delete the food_staff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''


fruits = ('apple', 'pear','banana')
vegetables = ('cabagge', 'gourd', 'lettuce')
animal_products = ('loin', 't-bone','chops')
food_stuff_tp = fruits + vegetables + animal_products
list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_tp[4],'is the middle item')
print(food_stuff_tp[0:3],'are the first 3 items')
## do del food_stuff_tp if you want to delete
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
Iceland = 'Iceland' in nordic_countries
Estonia = 'Estonia' in nordic_countries
print('check if Iceland is in the tuple',Iceland)
print('check if Estonia is in the tuple',Estonia)