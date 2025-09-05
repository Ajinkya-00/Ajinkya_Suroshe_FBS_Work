# Replace all occurrences of 'a' with $

str = input("Enter the string : ")
new_str = ""

for ch in str:
    if ch == 'a':
        new_str += '$'
    else:
        new_str += ch

print(new_str)