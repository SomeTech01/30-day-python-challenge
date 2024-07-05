'''' \t = 8 spaces 
var.expandtabs() = 8 spaces
var.expandtabs(1) = 1 space'''
challenge = 'thirty\tdays\tof\tpython'
print('Replacing tab or \\t with space of your choice')
print(challenge)
print('Default is 8 spaces using var.expandtables()')
print(challenge.expandtabs())   # 'thirty  days    of      python'
print('Can become a regular space if you use var.expandtables(1)')
print(challenge.expandtabs(1)) # 'thirty    days      of        python'