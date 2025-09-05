# Replace every blank space with -

str = input("Enter the string : ")
new_str = ""

for ch in str:
    if ch == " ":
        new_str += "-"
    else:
        new_str += ch

print(new_str)