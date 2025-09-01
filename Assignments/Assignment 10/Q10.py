li = [1, 2, 3, 4, 5, 2]
num = int(input("Enter the number to remove: "))
new_list = []

for i in li:
    if i != num:
        new_list.append(i)

print("After removal :",new_list)