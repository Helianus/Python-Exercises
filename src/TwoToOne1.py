s1 = "xyaabbbccccdefwwsadfhlgfdfhgskdghkdfzhgzjhgkdzhgfkxhgfkzhgkjfdhgizfghkzhgkzdhfgkz"
s2 = "xxxxyyyyabklmopqdfaiusfghskjghsjkdgbsdkgjbsdgbskdkfbnsdkhsgb"
# take 2 strings s1 and s2 including only letters from ato z. 
# Return a new sorted string, the longest possible, containing distinct letters
# This version is using bitwise
def longest(s1, s2):
    visited = 0
    s = s1 + s2
    result = ""
    for i in range(len(s)):
        shift = ord(s[i]) - ord('a')
        if visited & (1 << shift) == 0:
            visited = visited | (1 << shift)
    for shift in range(26):
        if ((visited >> shift) & 1 == 1):
            result += chr(shift + ord('a'))
    return result