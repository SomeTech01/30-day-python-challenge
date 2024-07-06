''' Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.'''

import os ## import os module

def list_of_hexa_colors(times): ## define a function
    list_of_hex = [] ## initialize a list 
    for i in range(times):  # loop using a user supplied legnth
        hex = os.urandom(3).hex() ##urandom generates random bytes suitable for cryptographic use. 3 is the bytes also equals to 6 characters(tested 1=2chars,2=4chars, so on).The hex() method converts the bytes object into a string of hexadecimal digits
        hex = ('#'+hex) ## add # to the generated hex
        list_of_hex.append(hex) #appends the generated hex to a list
    return list_of_hex          ## returns the list
print(list_of_hexa_colors(2))
print()

'''Write a function list_of_rgb_colors which returns any number of RGB colors in an array '''

import random ## import random module

def list_rgb_colors(length): ## define a  function
    rando = random.randint(0,255) #generate random int 3x
    rando1 = random.randint(0,255)
    rando2 = random.randint(0,255)
    
    list_of_rgb = [] # initialize a list
    for i in range(length): # loop using a user supplied legnth
        rgb = 'rgb',(rando,rando1,rando2) ## adds rgb and all the randomly generated int
        list_of_rgb.append(rgb) ## appends the generated var to a list
    return list_of_rgb #returns the list
print(list_rgb_colors(2))
print()
''' Write a function generate_colors which can generate any number of hexa or rgb colors.'''
import os,random
def list_of_hexa_colors(times):
    list_of_hex = []
    for i in range(times):
        hex = os.urandom(3).hex()
        hex = ('#'+hex)
        list_of_hex.append(hex)
    return list_of_hex

def list_rgb_colors(length):
    rando = random.randint(0,255)
    rando1 = random.randint(0,255)
    rando2 = random.randint(0,255)
    
    list_of_rgb = []
    for i in range(length):
        rgb = 'rgb',(rando,rando1,rando2)
        list_of_rgb.append(rgb)
    return list_of_rgb

def generate_colors(operations , x): ## define a function using the function above
    return operations(x)            ## returns the result of what the user chose between the two

print(generate_colors(list_rgb_colors, 1))