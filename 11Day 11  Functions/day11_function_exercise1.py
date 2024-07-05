#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two(x,y):
    print('total of:')
    return x + y
print(add_two(5,9))
print()
#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(radius):
    pi = 3.14
    print('are of the number is')
    return pi * radius * pi
print(area_of_circle(15))
print()
#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    try:
        return sum(nums)
    except: ValueError
    print('Please eneter a number')
print(add_all_nums(4.3,5.5,6))
print()
#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(C):
    print(C,'in Farenheit is:')
    try:
        return (C * 9/5)+32
    except: ValueError
    print('Please enter a number')
print(convert_celsius_to_fahrenheit(37.4))
print()

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']: ## doing month == 'december', 'january', 'february' doesnt work
        return 'Winter'                             ## putting it in alist to loop through will be better
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Please enter a valid month'
print(check_season('November'))
print()
#Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,x2,y1,y2):
    print('slope is:')
    return (y2 -y1) / (x2-x1) 
print(calculate_slope(3,5,2,6))
print()
#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratci_eqn(a,b,c,x):
    return (a*(x**2) + (b*x) + c) ## a(x) doesn't mean a*x
print(solve_quadratci_eqn(3,4,5,2))
print()
#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(*x):
    return list(x)
print(print_list(1,'test','IT','Cambodia'))
print()
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(*x):
    reversed = [] ## empty list
    for i in x: ## loop through the list
        reversed.append(i) ## append the supplied array to the empty list
    return reversed[::-1] ### Reversing a list using slicing technique. start range:end range: starting from the last on the list going to index 0
print(reverse_list(5,4,3,2,1,0))
print()
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list): ## *list will create a tuple
    capital = [] ## create an empty list
    for words in list: ## loops through the list provided
        capital.append(words.capitalize()) ## capitalizing and appendeng the loop'ed words to the empty list 
    return capital
lower_list = ['the', 'world','says', 'hello'] ## (1) decalre a list
print(capitalize_list_items(lower_list)) ##(2) use it as the param
print()
#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(original,add):
    added = []
    added.append(add)
    return original + added
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff,'Meat'))
print()
#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(original1,out):
    original1.remove(out)
    return original1

food_stuff1 = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff1,'Mango'))
print()
#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(p):
    count = 0 # Initialize a variable to store the sum of numbers
    for i in range(p+1):# Loop through numbers from 0 to p+1 = 6 or 1,2,3,4,5 . Python will not return the end
        count += i  # Add each number to count
    return count #return total count
print(sum_of_numbers(5))
print()
#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odd(p):
    count = 0 # Initialize a variable to store the sum of numbers
    for i in range(p+1):# Loop through numbers from 0 to p+1 = 6 or 1,2,3,4,5 . Python will not return the end
        if i%2 != 0: ## divided by 2 and with remainder it is odd
            count += i  # Add each number to count
    return count #return total count
print(sum_of_odd(5))
print()
#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(p):
    count = 0 # Initialize a variable to store the sum of numbers
    for i in range(p+1):# Loop through numbers from 0 to p+1 = 6 or 1,2,3,4,5 . Python will not return the end
        if i%2 == 0: ## divided by 2 and no remainder it is even
            count += i  # Add each number to count
    return count #return total count
print(sum_of_even(5))
print()