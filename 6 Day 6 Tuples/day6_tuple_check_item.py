''' tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True '''

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
orange = 'orange' in fruits 
print(f'check if there is \'orange\' in list: {orange}')
apple = 'apple' in fruits 
print(f'check if there is \'apple\' in list: {apple}')
print('if you try to append to the list with list[0 = str it will error out.\n!!Always read the error message to troubleshoot!!')
#fruits[0] = 'apple' = TypeError: 'tuple' object does not support item assignment