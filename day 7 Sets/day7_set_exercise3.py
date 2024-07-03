'''' Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.'''
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_convert = set(age)
print(type(age))
print(age)
print(type(age_convert))
print(age_convert)
print('length of age list is:',str(len(age)))
print('length of age set is:',str(len(age_convert)))
print('str are any character(A-Z,0-9,`,*,etc) that are written inside quotes')
print('list is a group of items within squre brackets [] that are mutable/modifiable')
print('tuple is a group of items within parenthesis () that are immutable/non-modifiable')
print('set is a group og items within curly bracket {} that are mutable/modifiable')

sentence = 'I am a teacher and I love to inspire and teach people.'
split_sentence = sentence.split()
print(split_sentence)
print('When duplicates are removed from the sentence, the set looks like this:',set(split_sentence))
