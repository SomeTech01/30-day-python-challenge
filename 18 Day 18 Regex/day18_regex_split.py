''' '''
import re
#eliminates new line and returns a list
## will not take a list to split. Use indexing/slicing instead
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
test = re.split('\n', txt)

