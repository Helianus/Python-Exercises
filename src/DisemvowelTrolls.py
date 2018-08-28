string = "This website is for losers LOL!"
def disemvowel(string):
    result = string.replace("a", "")
    result = result.replace("e", "")
    result = result.replace("i", "")
    result = result.replace("o", "")
    result = result.replace("u", "")
    result = result.replace("A", "")
    result = result.replace("E", "")
    result = result.replace("I", "")
    result = result.replace("O", "")
    result = result.replace("U", "")
    return result

print(disemvowel(string))