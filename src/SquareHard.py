# Square a integer, the hard way
n = int(input("Input an integer: "))
ans = 0
iterStill = abs(n)
# n^2 = n + n + .. + n
while (iterStill != 0):
    ans += abs(n)
    iterStill -= 1
print(str(n), "*", str(n), "=", str(ans))