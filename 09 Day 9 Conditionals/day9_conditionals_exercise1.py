'''Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
age = int(input()) also works'''

age = input(('What is your age?'))
age = (int(age))
if age >= 18:
    print('You are old enough to drive')
elif age < 18:
    print('You need', str(18 - age) ,'more years to learn to drive')
print()

''' 'Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
Output:
Enter your age: 30
You are 5 years older than me.'''
age1 = input(('What is your age?'))
age1 = (int(age1))
my_age = 21
if my_age > age1:
    print('I am', str(my_age - age1), 'years older than you')
elif my_age == age1:
    print('We are twins!!')
else:
    print('You are', str(age1 - my_age), 'years older than me')

'''Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3'''
one = int(input('Enter the first number:'))
two = int(input('Enter the second number:'))
if one > two:
    print(f'{one} is greater than {two}')
elif one - two == 0:
    print('They are equal')
else:
    print(f'{one} is less than {two}')
print()


