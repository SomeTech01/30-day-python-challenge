'''' 

Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies
'''
new_list = []
new_list1 = [1,2,3,4,5]
print(len(new_list), len(new_list1), sep=' & ')
print(new_list1[::2])
mixed_data_types = ['Test', 24, 57,'Married','New street']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(mixed_data_types, it_companies, sep='\n')
print(len(it_companies))
print(it_companies[0::3])
it_companies[0] = 'Neutron'
print(it_companies)

print()
'''

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list
'''

it_companies.append('Facebook')
print(it_companies)
it_companies.insert(3, 'Inserted Company')
print(it_companies)
## replace the first element to upper case ##
caps = str(it_companies[0])
caps = caps.upper()
it_companies.remove('Neutron')
it_companies.insert(0, caps)
print(it_companies)
####
print('# '.join(it_companies))
print('IBM' in it_companies)
## sort out list
it_companies.sort()
print(it_companies)
## sort in reverse
it_companies.sort(reverse=True)
print(it_companies)
print(it_companies[3:])
print(it_companies[0:-3])
first_3_companies = it_companies[0:3]
last_3_companies = it_companies[-3:]
print(first_3_companies + last_3_companies)

''' 

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
'''

print()
del it_companies[0] #Remove the first IT company from the list
print(it_companies)
del it_companies[3:5] ##Remove the middle IT company or companies from the list
print(it_companies)
del it_companies[-1] # Remove the last IT company from the list
print(it_companies)
it_companies.clear()
print(it_companies) ## clears the list
del it_companies ## errors out