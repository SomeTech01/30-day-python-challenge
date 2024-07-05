''''Write a code which gives grade to students according to theirs 
scores: 
80-100, A
70-79, B
60-69, C
50-59, D
0-49, F'''

grades = int(input('Please enter your score to know your grade:'))
if grades >=80 and grades <= 100:
    print('A')
elif grades >= 70 and grades <= 79:
    print('B')
elif grades >= 60 and grades <= 69:
    print('C')
elif grades >= 50 and grades <= 59:
    print('D')
elif grades == 0  and grades <= 49:
    print('F')
else:
    print('Error: please check input. You can\'t have a score of more than 100')
print()
''' Check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. 
March, April or May, the season is Spring 
June, July or August, the season is Summer'''

check_season = input('What month is it?')
check = check_season.lower()
if check == 'december' or check == 'january' or check =='febuary':
    print('The season today is: Winter')
if check == 'march' or check == 'april' or check =='may':
    print('The season today is: Sprint')
if check == 'june' or check == 'july' or check =='august':
    print('The season today is: Summer')
if check == 'september' or check == 'october' or check =='november':
    print('The season today is: Winter')
else:
    print('Error:Please check if the input. There are 12 only months in a year')
print()

''' If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')'''

user_fruit = str(input('Please eneter a fruit:'))
fruits = ['banana', 'orange', 'mango', 'lemon']

if user_fruit in fruits:
    print('That fruit already exist in the list')
elif user_fruit not in fruits:
    fruits.append(user_fruit)
    print('Thank you for the addition. This is the fruit basket now:')
    print(fruits)
else:
    print('Please talk to the dev something may be broken')
print()


