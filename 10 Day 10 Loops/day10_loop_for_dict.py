''' for iterator in dct:
    code goes here'''

person = {
    'first_name':'Test',
    'last_name':'IT',
    'age':250,
    'country':'Cambodia',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:  ## loops through the keys
    print(key)
print()

value_person = person.values() ## loops through values
for value in value_person:
    print(value)
print()

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
    

