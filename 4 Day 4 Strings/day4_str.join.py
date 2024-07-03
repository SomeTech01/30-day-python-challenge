''' 'delimter'.join(var) to print out the content of a var seprated by the delimeter '''
print('join(): Returns a concatenated string')
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(web_tech)
print("'delimter'.join(var)")
print('result = \' \'.join(web_tech)')
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
print()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(web_tech)
print('result = \'#\'.join(web_tech)')
result = '#'.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'