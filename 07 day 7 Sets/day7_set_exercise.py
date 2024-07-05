'''Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard'''
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(it_companies)
print(A)
print(B)
print(age)
print('The length of it_compnies:',str(len(it_companies)))
add_company = it_companies.add('Twitter')
print('Twitter added to the IT companies set:',it_companies)
more_companies = {'Crowdstrike','Alibaba','More'}
it_companies.update(more_companies)
print('More companies added to the IT companies set:',it_companies)
it_companies.pop()
print('Random company was removed from the set:', it_companies)
print('remove method will cause an error if the item is not in the list, while discard method will not')