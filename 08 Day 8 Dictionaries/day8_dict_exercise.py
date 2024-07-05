''' Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries'''

print('Creating an empty dict then adding k:v after')
dog ={}

dog['name'] = 'whitey'
dog['color'] = 'brown'
dog['legs'] = 4
dog['breed'] = 'new kind'
dog['age'] = '1 day old'
print(dog)
print()
print('student dict')
student = {'first_name':'student',
        'last_mame': 'council',
        'gender': 'prefer not to say',
        'age': 'still young',
        'marital status':'doing good',
        'skills':['playing solitaire'], ## putting the value of skill in [] initializes it as a list
        'country':'Cambodia',              ## more values can be added to it
'city':'Pyoyang', 'address':'close by'
}
print('The length of the student dictionary is:',str(len(student)))
print('The student knows how to:',student['skills'])
print((student.items()))
print(type(list(student)))
student['skills'].append('sleeping standing up')
print(student)
print()
keys = student.keys()
values = student.values()
print('The keys in the dictionary are:',keys)
print('The values in the dictionary are:',values)
print()
print((student.items()))
print()
dog.pop('age')
print(dog)
del student
#print(student) ## errors out not defined