''' for iterator in range(start, end, step)
range() function is used list of numbers
By default it starts from 0 and the increment is 1
needs at least 1 argument (end)'''
for number in range(11):
    print(number) 
print()

## create sequence using range
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print()
## 3rd number is the step
lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

