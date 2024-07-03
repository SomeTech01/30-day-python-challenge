first_name = 'Test'
last_name = 'secret'
full_name = first_name + ' ' +last_name
country = 'Cambodia'
city = 'Poipet'
age = 99
year = 2024
is_married = True
is_light_on = True
schedule , meeting, duration = True, True , '45 mins'
'''Check the data type of all your variables using type() built-in function'''
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(schedule))
print(type(meeting))
print(type(duration))
'''Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name'''
print('*******************************')
print('length of first name is ' + (str(len(first_name))))
print('length of last name is ' + str(len(last_name)))
print('The difference of first and lastname is: ' + str(len(first_name) - len(last_name)))

print('*******************************')

'''Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp'''

num_one = 5
num_two = 4
total = num_one + num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

print(total)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)
print('*******************************')

'''The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.'''


radius = 30
area_of_circle = 3.14*((radius)**2)
circum_of_circle = 2 * 3.14 * 30
print('Area is = ' + str(area_of_circle) + ' square meters')
print('Circumference is = '+ str(circum_of_circle)+ ' meters')

print('*******************************')
"""Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names"""

print("What is first name?")
ask_name = input()
print("What is your  last name?")
ask_last = input()
print('How old are you?')
ask_age = input()
print('What country are you from?')
ask_country = input()
print('Hello ' + ask_name + ' ' + ask_last + '!')
print(f"You are {ask_age}, that is nice!")
print(f"How is the weather there at {ask_country}?")