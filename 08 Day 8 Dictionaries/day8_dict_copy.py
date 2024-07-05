''' 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}'''
person = {
    'first_name':'Test',
    'last_name':'IT',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(person)
print()
copy_person = person.copy()
print(copy_person)

print('First dict\'s id:',id(person)) 
print('Copy of the dict\'s id:',id(copy_person))