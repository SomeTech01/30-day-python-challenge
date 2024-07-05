#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)
print()
count = 0
while count < 11:
    print(count)
    count += 1
print()
#Iterate 10 to 0 using for loop, do the same using while loop.
for y in reversed(range(11)):
    print(y)
print()
counter = 10
while counter > -1:
    print(counter)
    counter -= 1
print()
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#  #
#  ##
#  ###
#  ####
#  #####
#  ######
#  #######
for z in range(8):
    print(z * '#')
print()
#Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for rows in range(8): #Outer Loop (Rows): The outer loop runs 8 times, once for each row.
    for columns in range(8): #Inner Loop (Columns): Inside the outer loop, the inner loop also runs 8 times, once for each column.
        print('#',end='') #Print # with end='': The print('#', end='') statement prints the # character without moving to a new line. The end='' part means that instead of the default behavior of print (which is to move to a new line after printing), it will stay on the same line.
    print() #Move to the Next Line: After the inner loop completes (i.e., after printing 8 # characters), the print() statement (without any arguments) is used to move to the next line.
#https://pynative.com/print-pattern-python-examples/
print()
#Print the following pattern:

#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
num = 0
while num <11:
    print(num,'x', num, '=',(num*num))
    num += 1
    
print()

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for items in list:
    print(items)
print()
#Use for loop to iterate from 0 to 100 and print only even numbers
for a in range(0,101,2):
    print(a)
print()
#Use for loop to iterate from 0 to 100 and print only odd numbers
for b in range(1,100,2):
    print(b)