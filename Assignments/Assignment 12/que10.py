# Compare two strings and display the larger one

s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")

len1 = 0
len2 = 0

for ch in s1:
    len1 += 1

for ch in s2:
    len2 += 1

if len1 > len2:
    print(s1)
else:
    print(s2)