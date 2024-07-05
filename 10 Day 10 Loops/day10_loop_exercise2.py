#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.
results =[]
for i in range(101):
    results.append(i)
print('Total of iterated numbers 0 to 100 is:',sum(results))

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#The sum of all evens is 2550. And the sum of all odds is 2500.
result_even = []
result_odd = []

for x in range(0,101,2):
    result_even.append(x)
for y in range(1,101,2):
    result_odd.append(y)
print('Total of iterated even numbers is:',sum(result_even))
print('Total of iterated odd numbers is:',sum(result_odd))