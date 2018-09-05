# Given an array of integers, remove the smallest value. 
# Do not mutate the original array/list. 
# If there are multiple elements with the same value, 
# remove the one with a lower index. 
# If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.

def remove_smallest(numbers):
    result = []
    if numbers == []:
        return numbers
    else:
        mini = min(numbers)
        for i in range(len(numbers)):
            if numbers[i] == mini:
                result = numbers[:i] + numbers[i+1:]
                break
    return result

print(remove_smallest([254, 179, 388, 216, 315, 43, 78, 281]))