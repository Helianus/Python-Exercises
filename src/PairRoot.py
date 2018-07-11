# 0 < pwr < 6 and root^pwr = user input
n = int(input("Enter an integer: "))
pwd, root = 0, 0
while root <= n:
    pwd += 1
    if pwd == 6:
        pwd = 1
        root += 1
    if root ** pwd == n:
        print(root, "^", pwd, "is", n)
