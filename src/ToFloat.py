# Convert a string separated by comma into a float
s = '1.23,2.4,3.123'
total = 0
for i in s.split(','):
    total += float(i)
print(total)