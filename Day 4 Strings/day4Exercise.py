print('''Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split())''')

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding'))
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
new = (company.replace('Coding', 'Python'))
print(new.replace('All', 'Everyone'))
print(company.split())
print()
print('''"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction''')

orgs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(orgs.split(', '))
print(company[0])
print(company[-1])
print(company[10])
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))
conjuctions = 'You cannot end a sentence with because because because is a conjunction'
print(conjuctions.find('because'))
print(conjuctions.rindex('because'))
print(conjuctions[31:54])
print()
print('''Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.''')

print(company.startswith('Coding'))
print(company.endswith('Coding'))
new_company = '   Coding For All      ' 
print(new_company.strip())

language = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(language))

print('''Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144''')
print()
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nTeacher\t250\tFinland\tHelsinki')

print()
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')