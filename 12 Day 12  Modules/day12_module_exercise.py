''' import modules
define a function
random.choices - generate a list of characters randomly chosen from the concatenation of string.ascii_letters
'0123456789' - added to the random upper and lower case string
k=length specifies that random.choices should return a list of length characters.
''.join(...)  - joins everything in a single string
return the generated string'''
import random, string
def random_user_id(length): 

    user_id = ''.join(random.choices(string.ascii_letters + '0123456789', k= length))
    return user_id
print(random_user_id(6))
print()
''' Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.'''
''' outside a function when the for loop runs it automatically prints out user_id depending on the range
taking out the empty list creaks the code
not saving the call out to a var and looping through it returns a list of the id not one per line'''
def user_id_gen_by_user():
    char = int(input("Enter the number of characters for each ID: ")) ##ask user for number of char
    num_ids = int(input("Enter the number of IDs to generate: ")) ## ask user for number of id
    
    ids = [] ## create an empty list
    for _ in range(num_ids): #Iterates num_ids times to generate that many IDs.
        user_id = ''.join(random.choices(string.ascii_letters + '0123456789', k=char))  
        ids.append(user_id) ## appends generated user_id to the list
    
    return ids  ## this will return a list only
gen_id = user_id_gen_by_user() ## if you want to return the string one per line, assign the call out to a var
for i in gen_id: ## loop through the var and print it
    print(i)
print()

''' Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form'''

def rgb_color_gen():
    rando = random.randint(0,255)
    rando1 = random.randint(0,255)
    rando2 = random.randint(0,255)
    return f'rgb({rando},{rando1},{rando2})'
print(rgb_color_gen())