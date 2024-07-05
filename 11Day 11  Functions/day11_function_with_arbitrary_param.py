''' def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)'''

def sum_all_nums(*nums): ##*args accepts multi args
    total = 0
    for num in nums: # 2,3,5
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10