#Complete the function that accepts a string parameter, 
# and reverses each word in the string. 
# All spaces in the string should be retained.

def reverse_words(text):
    lst = text.split(" ")
    result = " "
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    result = " ".join(lst)
    return result
