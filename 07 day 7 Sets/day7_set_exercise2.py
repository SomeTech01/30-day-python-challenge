''' Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A)
print(B)
A.update(B)
print('When both sets are joined using update:',A ,'\nDuplicates are not returned.')
a_sub_b = A.issubset(B)
print('Is A subset of B:',a_sub_b)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
a_union =A.union(B)
print(a_union) ##same results as update,no duplicates returned
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
b_union =B.union(A) ## tested re-declaring sets same results
print(b_union) 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
dif = A.symmetric_difference(B)
print('Symtrtic difference between both sets:',dif) ## A will have nothing as 'remainder' + B with 28 27 as 'remainder'
del A #errors out if printed
del B
