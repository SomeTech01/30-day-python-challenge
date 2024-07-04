'''' dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) '''

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
print(type(person))
print(person)
print()
print('First name is:',person['first_name']) 
print('He is from:',person['country'])    
print('He knows:',person['skills'])     
print('His first skill is:',person['skills'][0])  
print('His address is:',person['address']['street']) 
print('I returned the values using dict[key]')
print()
''' can also be done using
dict.get('key')'''

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) 
print('This time around I used dict.get(key) to return the values')