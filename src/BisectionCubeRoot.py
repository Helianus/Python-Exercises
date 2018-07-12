# Using bisection search to approximate Cube root
def BisectionCubeRoot():
    x = float(input("Enter an number: "))
    epsilon = 0.01
    low = 0.0
    high = max(0.0, abs(x))
    ans = (low + high) / 2.0
    numGuesses = 0
    while abs(ans ** 3 - abs(x)) >= epsilon:
        numGuesses += 1
        print("low=", low, "high=", high, "ans=", ans)
        if ans ** 3 < abs(x):
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
    print("numGuesses=", numGuesses)
    if x < 0:
        print(-ans, "is the square root of", x)
    else:
        print(ans, "is the square root of", x)

if __name__ == "__main__":
    BisectionCubeRoot()