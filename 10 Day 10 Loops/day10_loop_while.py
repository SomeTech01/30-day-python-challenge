'''while condition:
    code goes here
    
    while condition:
    code goes here
else:
    code goes here'''

## code runs starting from the counter 0 until it gets to 5 then stops
## while it has not reached 5 it will add 1 to the counter and print itself then it stops at 5(5 will not be printed)
count = 0
while count < 5:
    print(count)
    count = count + 1
print()   
# loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)