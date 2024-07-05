''' def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)'''

def greetings (name = 'Peter'): ## param value explicitly declared/defaulted 
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings()) ## returns the message of greetings.Param explicitly declared
print(greetings('Test'))  ## will disregard the exlicitly declared param value in the fnction
print()

def generate_full_name (first_name = 'Test', last_name = 'IT'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name()) ## returns the declared/default param
print(generate_full_name('David','Smith')) ##'overwrite' the default
print()
def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1821)) ##'overwrite' the default param 
print()

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon