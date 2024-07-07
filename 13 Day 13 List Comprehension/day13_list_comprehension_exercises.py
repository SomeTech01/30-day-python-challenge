'''Filter only negative and zero in the list using list comprehension'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives = [i for i in numbers if i < 0]
print(negatives)
print()

''' Flatten the following list of lists of lists to a one dimensional list 
output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
have to be done twice  cause arrays are in square brackets twice
longform of flat is:
for sublist in list:
    x in sublist:
        flat.append(x)'''

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat = [x for sublist in list_of_lists for x in sublist]
flat1= [x for xsublist in flat for x in xsublist]

print("List of lists:", list_of_lists)
print('First try of flattening out:', flat)
print("Flattened list:", flat1)
print()
''' [(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
result = []
for i in range(11):  # Iterate over numbers 0 through 10
    # Calculate the values for the tuple
    tuple_values = (i, 1, i, i**2, i**3, i**4, i**5)
    # Append the tuple to the result list
    result.append(tuple_values)
'''
##The tuple (i, 1, i, i**2, i**3, i**4, i**5) is the expression
##range(11) generates numbers from 0 to 10 (inclusive).

list1 = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(list1)
print()
''' countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]'''

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#flatten out
flat = [j for i in countries for j in i]
# Transform each tuple into a dictionary
result = [{'country': country.upper(), 'city': city.upper()} for country, city in flat] #{'country': country.upper(), 'city': city.upper()} is a dictionary comprehension that iterates through each tuple (country, city) in flat. https://www.geeksforgeeks.org/python-dictionary-comprehension/
print(flat)
print(result)
print()
''' names = [[('Test', 'IT')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Test IT', 'David Smith', 'Donald Trump', 'Bill Gates']

flat2 = []
for sublist in names:
    for pair in sublist:
        flat2.append(pair)

result = []
for pair in flat2:
    # Join the tuple elements with a space
    joined_name = ' '.join(pair)
    # Append the joined string to the result list
    result.append(joined_name)'''

names = [[('Test', 'IT')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

flat2 = [pair for sublist in names for pair in sublist] ## flaten the list and converts it to tupples
y = [' '.join(pair) for pair in flat2] ## prcocess for 'element' in list


print(flat2)
print(y)
print()
''' Write a lambda function which can solve a slope or y-intercept of linear functions'''
slope = lambda x1,x2,y1,y2 : (y2-y1) /(x2-x1)
print(slope(5,4,6,3))
