'''def foo1(n): ## foo1 runs uses 10 as arg (2)
    return n + 1 ## adds 1 to it making it 11 (3)
def foo2(m,x)  ## now foo2 has an arg foo2(11) (4)
    return m(x) ## retruns 11 (5)
print(foo2(foo1,10)) ## args inside are declared for foo1 (1)
'''
def square_number(n): 
    return n * n 
def do_something(f,x): 
    return f(x) 
print(do_something(square_number, 3)) 
print()

'''When you call do_operation(add_five, 10), here's what happens:

    Passing Arguments:
        add_five is passed as operation.
        10 is passed as number.

    Execution Inside do_operation:
        do_operation then calls operation(number).
        This translates to add_five(10).

    Function Execution (add_five(10)):
        Inside add_five, the argument x is 10.
        add_five(10) calculates 10 + 5, resulting in 15.

    Return Value:
        do_operation returns the result of operation(number), which is 15 in this case.'''

# Define a function that adds 5 to a number
def add_five(x): 
    return x + 5 

# Define a function that subtracts 3 from a number
def subtract_three(x):
    return x - 3

# Define a function that performs an operation on a number
def do_operation(operation, x):  
    return operation(x) 

# Example usage:
result1 = do_operation(add_five, 10)  
print("Result 1:", result1)  # Output: Result 1: 15

result2 = do_operation(subtract_three, 8)
print("Result 2:", result2)  # Output: Result 2: 5
