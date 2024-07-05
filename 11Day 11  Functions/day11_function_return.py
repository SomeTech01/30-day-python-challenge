'''if a function does not have a return statement, the value of the function is None 
print the function call if there is a return'''

def generate_full_name ():
    first_name = 'Test'
    last_name = 'IT'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print()
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
print()
''' return str'''
def print_name(firstname):
    return firstname
print(print_name('Test')) # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_full_name(firstname='Test', lastname='IT'))
print()
''' return numbers'''
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age:',calculate_age(2019, 1819))
print()
'''return boolean'''
def is_even (n):
    if n % 2 == 0:
        print(n,'is even:')# prints first if the if statement is True
        return True    # return stops further execution of the function, similar to break 
    else:
        return False ##returns if condition is False
print(is_even(10)) # True
print(is_even(7)) # False
print(is_even(5)) 
print(is_even(2)) 
print()
'''return list'''
def find_even_numbers(n):
    evens = []
    print('even numbers from 0 -',n,':')
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))