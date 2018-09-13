# Find the sum of the odd numbers within an array, 
# after cubing the initial integers. 
# This function will return undefined (NULL in PHP) if any of the values aren't numbers.

def cube_odd(arr):
    #your code here - return None if at least a value is not an integer
    ans = 0
    for i in range(len(arr)):
        if isinstance(arr[i], str):
            return None
        elif (arr[i] % 2 != 0):
            ans += (arr[i])**3
    return ans


print(cube_odd([6, 6, -6, 7, -6, -10, -9, -6]))