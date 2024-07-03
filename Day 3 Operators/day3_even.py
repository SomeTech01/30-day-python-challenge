"""Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10"""
number =10
even = number % 2 == 0
print(f'Using number %2 == 0. Is 10 even? {even}')
print('Floor division of 7 and 3 is ',7//3)
print('Is type(10) == type("10")', type(10) == type('10'))
print('After converting Str > float > int. Is int("9.8") == 10: ' , int(float("9.8")) == 10)
