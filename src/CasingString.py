#Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, 
# but they are not capitalized in the same way he originally typed them.

def toJadenCase(string):
    string = string.lower()
    lst = string.split(" ")
    result = ""
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()
    result = " ".join(lst)
    return result

print(toJadenCase("Young Jaden: Here'S The Deal For Every Time Out You Give Me, You'Ll Give Me 15 Dollars For Therapy When I Get Older"))