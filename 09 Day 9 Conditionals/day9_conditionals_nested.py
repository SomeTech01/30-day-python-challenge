''' if condition:
    code
    if condition:
    code'''

a = 5
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is an odd number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')