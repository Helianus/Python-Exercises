# Given a list of digits, return the smallest number that could be formed from these digits, 
# using the digits only once ( ignore duplicates).
# Notes: Only positive integers will be passed to the function (> 0 ), no negatives or zeros.
# Input >> Output Examples
# 1- minValue ({1, 3, 1})  ==> return (13)
# Explanation:

def min_value(digits):
    lst = sorted(list(set(digits)))
    return int("".join(map(str, lst)))
    

print(min_value({1,3,1}))