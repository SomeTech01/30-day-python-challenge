#Write a pattern which identifies if a string is a valid python variable
''' is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

r'^[a-zA-Z_][a-zA-Z0-9_]*$':

^ asserts the start of the string.
[a-zA-Z_] matches any letter (a-z or A-Z) or underscore (_) at the beginning.
[a-zA-Z0-9_]* matches zero or more occurrences of letters (a-z or A-Z), digits (0-9), or underscores (_).
$ asserts the end of the string.'''

import re

def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'  ## sets a pattern
    return re.match(pattern, variable) is not None ##  is not None for error handling

# Test cases
print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True
print()

'''Clean the text
sentence = %I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?

print(clean_text(sentence));
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]'''

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(var): ## define a function
    pattern1 = r'[%@$#&*;!^_|~,-.?]'#pattern for special characters. You will have to escape accordingly. Edit one at a time to avoid error and easy debugging
    return re.sub(pattern1,'',var) ## returns the substituted the pattern with nothing on the provided var


cleaned = clean_text(sentence) ## save the call out in to a function
print(cleaned) ## print out

from collections import Counter ##
def most_frequent(var):
    split_first = var.split() ## list all the words in the string
    counter = Counter(split_first) ##pass the split string to counter
    return  counter.most_common(10) ## k=3 that most_common() encountered and will produce
    
print(most_frequent(cleaned)) # If you are using a proper sentence (with punctuation marks),teacher and teaching will appear only as one because of the punctuation teacher, != teaching? 