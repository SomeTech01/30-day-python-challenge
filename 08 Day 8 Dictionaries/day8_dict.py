'''A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
use curly brackets, {} or the dict() built-in function
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}'''

person = {
    'first_name':'Test',
    'last_name':'IT',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(type(person))
print(person)
