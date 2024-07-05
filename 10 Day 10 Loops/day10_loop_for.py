''' for iterator in lst:
    code goes here'''

#loops through the list  
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

print()
##loops through str
language = 'Python'
for letter in language:
    print(letter)
print()
for i in range(len(language)): ## for i in range(6): = 'Python' is 0-5 characters counted as 6
    print(language[i])  ##Access each character by index: Inside the loop, i takes on each value from 0 to 5, and language[i] accesses the character at that position in the string.
'''Here's what happens step-by-step:

Iteration 1: i is 0, language[i] is 'P'.
Iteration 2: i is 1, language[i] is 'y'.
Iteration 3: i is 2, language[i] is 't'.
Iteration 4: i is 3, language[i] is 'h'.
Iteration 5: i is 4, language[i] is 'o'.
Iteration 6: i is 5, language[i] is 'n'.'''