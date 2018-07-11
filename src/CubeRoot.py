# Find the cube root of a perfect cube
n = int(input("Enter an integer: "))
ans = 0
while ans ** 3 < abs(n):
    ans += 1
if ans ** 3 != abs(n):
    print(n, "is not a perfect cube")
else:
    if n < 0:
        ans = -ans
    print("Cube root of", n, "is", ans)