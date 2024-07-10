'''  Returns a list containing all matches'''
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']



## if you dont want to use re.I regex and |/or can be used
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
