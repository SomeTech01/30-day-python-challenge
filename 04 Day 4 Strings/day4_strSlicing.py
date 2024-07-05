''' var[start index range: end index range] !!end index range is not called out!!'''
language = 'Python'
print(language)
print('First 3 indices using 0:3')
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
print('Last 3 indices using 3:6')
last_three = language[3:6]
print(last_three) # hon
# Another way
print('Last 3 indices using -3')
last_three = language[-3:]
print(last_three)   # hon
print('Last 3 indices using 3:')
last_three = language[3:]
print(last_three)   # hon

print()

'''SKipping characters while slicing
var[start index range: end index range: how many skips]'''
language = 'Python'
pto = language[0:6:2] #
print('Skips characters by 2 from index 0:6')
print('To do this use var.[indexrange:skip by how many]')
print('var.[0:6:2]')
print(pto) # Pto