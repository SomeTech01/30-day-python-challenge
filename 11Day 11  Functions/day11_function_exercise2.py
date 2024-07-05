#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    
    
    for i in range(num + 1): ## loops through the number add 1 so the given will be included
        if i % 2 == 0: ##check if it is even
            even_count += 1 ## counts the even.Everytime the modulo = 0, 1 is added to even_count 
        else:
            odd_count += 1  ## if answer is not 0 its odd. 1 is added the odd_count
            
    return (f'The number of evens are: {even_count}\nThe number of odds are: {odd_count}')

print(evens_and_odds(100))
print()
#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
import math
def factorial(number):
    return math.factorial(number)
print(factorial(9))

##Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(check):
    if len(check) == 0:
        return 'It is empty'
    else:
        return 'Check the variable it has something in it'
var = []
print(is_empty(var))
print()
#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

import numpy,statistics    
def calculate_mean(num):
    mean = numpy.mean(num)
    return f'The mean of the given numbers is: {mean}'
def calculate_median(num):
    median = numpy.median(num)
    return f'The mean of the given numbers is: {median}'
def calculate_mode(num):
    mode = statistics.mode(num)
    return f'The mean of the given numbers is: {mode}'
def calculate_range(num):
    mini = min(num)
    maxi = max(num)
    return f'The range is from {mini} to {maxi}'
def calculate_variance(num):
    vari = statistics.variance(num)
    return f'The variance is: {vari}'
def calculate_std(num):
    statdev = statistics.stdev(num)
    return f'The standard deviation is: {statdev}'
list = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
print(calculate_mean(list))
print(calculate_median(list))
print(calculate_mode(list))
print(calculate_range(list))
print(calculate_variance(list))
print(calculate_std(list))