'''   # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))'''

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Test'))
print()

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))
print()

def square_number(x):
    return x * x
print(square_number(2))
print()

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

print()

def sum_of_numbers(n): ## if n=10 the range is 11.
    total = 0           ## counter 
    for i in range(n+1): ## loop 0-10
        total+=i        ## increase loop by 1
    return total        ## return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050