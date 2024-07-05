'''   # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))'''

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Test','IT')) ##first str is to first param, 2nd str is to 2nd param

print()

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9)) ##first str is to first param, 2nd str is to 2nd param

print()

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819)) ##first str is to first param, 2nd str is to 2nd param

print()

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first. Parenthesis will be multiplied first before converting to str.
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81)) ##first str is to first param, 2nd str is to 2nd param