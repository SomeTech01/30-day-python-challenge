''' Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list'''
import random

def shuffle_list(x):
    shuffled = x[:] #creates a copy of the list x. The [:] slicing notation copies all the elements of x into a new list called shuffled_list. This ensures that we don't modify the original list x. ## copy.copy(x) did not work
    random.shuffle(shuffled)  ## shuffles the copied list
    return shuffled # returns the shuffled copied list
    
list1 = [1,2,3,4,5]
print(shuffle_list(list1))

''' Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.'''

import random

def array_rando():
    uniq  = random.sample(range(0,9),7) #Syntax : random.sample(sequence, k) sequence = Can be a list, tuple, string, or set; k= length
    return uniq

print(array_rando())