''' for x in y: ## loop through items in y and name it x
    for t in x: ## loop through the item in x and name it y
        print(t)'''
        
person = {
    'first_name': 'Test',
    'last_name': 'IT',
    'age': 250,
    'country': 'Cambodia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)