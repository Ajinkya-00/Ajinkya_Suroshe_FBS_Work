# Remove the nth index character

str = input("Enter the string : ")
ind = int(input("Enter the index value to remove : "))
new_str = ""

for i in range(len(str)):
    if i != ind:
        new_str += str[i]

print(new_str)