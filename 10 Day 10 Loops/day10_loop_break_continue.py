''' use break when we like to get out of or stop the loop.
while condition:
    code goes here
    if another_condition:
        break'''

## counter at 0. Condition is to add 1 to counter and print itself  until it reaches 5(or less than 5)
##if statement within the code block saying if the counter reaches 3 break/stop the code
## python 0,1,2 = 3 counts > break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
print()
'''while condition:
    code goes here
    if another_condition:
        continue
use continue when we like to skip some of the steps in the iteration of the loop'''


count = 0 ## counter at 0. 
while count < 5: #Condition runs until it reaches 5
    if count == 3: #Check if count is 3: Inside the loop, we check if count is equal to 3. Will be true cause the condition counts from 0 to 4.
        count = count + 1 #If count is 3, we increase count by 1 and use continue to skip the rest of the loop and start the next iteration immediately.
        continue ##continue the code block
    print(count) ## print count
    count = count + 1 ## add 1 to count
## The numbers are printed in ascending order because of the way the count variable is incremented and checked within the loop
## The numbers are printed in the order they are incremented, starting from 0 up to 4, but skipping 3 because of the continue statement

'''for iterator in sequence:
    code goes here
    if condition:
        break'''
print()
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)  #(1)print number
    if number == 3:
        continue
    if number != 5: ## (2)as long as the is not 5
        print('Next number should be ', number + 1)  ## print the statement +1 #(3) loops through those 2 codes until condtition is met
    else: #(4) if it gets to 5 
        print("loop's end") # print the end
print('outside the loop') ## nice way of saying the program has ended


