def high_and_low(numbers):
    # In this little assignment you are given a string of space separated numbers, 
    # and have to return the highest and lowest number.
    result = [int(x) for x in numbers.split()]
    string = str(max(result)) + " " + str(min(result))
    return string

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))