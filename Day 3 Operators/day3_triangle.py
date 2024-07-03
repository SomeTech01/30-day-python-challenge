"""Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)."""

age = 35
height = 3.15
complex_number = 1j

print('Enter Base')
base = input()
print('Enter hegiht')
triangle_height = input()
try:
    area = 0.5 * int(base) * int(triangle_height)
except: ValueError
print(f'The area of the triangle is {area}')

print()
"""Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)."""
a = int(input("What is side a?"))
b = int(input("What is side b?"))
c = int(input("What is side c?"))
perimeter = a + b + c
print('The perimeter of the triangle is ',perimeter)
