''' dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5 or
dct['keys5'].append('value5') '''

person = {
    'first_name':'Test',
    'last_name':'IT',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], ## initialized as a list so values can be appended
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print()
print(person['skills'])
person['skills'].append('HTML')
print('Updated dict after using dict.[key].append(\'new item\'):',person['skills'])
print()
print(person)
person['job_title'] = 'Instructor'
print('Added job title to the dict')
print('Updated dict after using dict[key] = value:',person)