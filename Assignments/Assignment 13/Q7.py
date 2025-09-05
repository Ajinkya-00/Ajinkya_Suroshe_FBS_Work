# Remove a Given Key from a Dictionary

dict = {1:1, 2:2, 3:3, 4:4, 5:5}
remove_key = int(input("Enter the key to remove : "))

new_dict = {}

for i in dict:
    if i != remove_key:
        new_dict[i] = dict[i]

print(new_dict)
