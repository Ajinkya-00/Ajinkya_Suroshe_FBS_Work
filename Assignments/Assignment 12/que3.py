# Detect if two strings are anagrams

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")

def sort_string(st):
    chars = list(st)
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            if chars[i] > chars[j]:
                chars[i], chars[j] = chars[j], chars[i]
    
    res = ""
    for ch in chars:
        res += ch
    return res

if sort_string(s1) == sort_string(s2):
    print("String is Anagram")
else:
    print("String is not Anagram")