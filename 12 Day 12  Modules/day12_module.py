''' A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base'''

''' # mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname'''

''' # main.py file
import mymodule
print(mymodule.generate_full_name('Test', 'IT'))'''

'''# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Test','IT'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname']) '''

''' # main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])'''

