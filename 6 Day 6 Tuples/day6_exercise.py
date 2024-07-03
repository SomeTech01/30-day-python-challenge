'''Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Unpack siblings and parents from family_members'''


new = ()
brothers = ('John','Jeremy','Jericho')
sisters = ('Peanut','Pooh','Pearl')
siblings = brothers + sisters
print(brothers)
print(sisters)
print(f'combined tuple of brothers and sisters: {siblings}.\nnew tuple = tuple+ tuple')
print('Total number of siblings: ', str(len(siblings)))
print()
family_members = list(siblings)
family_members.insert(0, 'Father')
family_members.insert(1, 'Mother')
family_members = tuple(family_members)
print('After converting the tuple to a list, the items are modified to add Father and Mother.\nThen, it was converted back to tuple.\nHere is he new tuple:\n',family_members)

print()
family_members = ('Father', 'Mother', 'John', 'Jeremy', 'Jericho', 'Peanut', 'Pooh', 'Pearl')
parent1, parent2,*sibling, family=family_members
print('Unpacking the tuple as parent1 , parent2, sibling:')
print(parent1)
print(parent2)
print(sibling)