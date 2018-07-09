# Find the max odd number among user inputs
n = int(input("Input an range: "))
maxOdd = None
for _ in range(n):
    value = int(input("Enter a value: "))
    if (value % 2 and (maxOdd is None or value > maxOdd)):
        maxOdd = value
if maxOdd:
    print("The largest odd number among them is " + str(maxOdd) + ".")
else:
    print("There is no largest odd number among them.")       