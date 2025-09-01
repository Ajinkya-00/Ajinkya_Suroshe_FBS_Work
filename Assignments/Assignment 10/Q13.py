li = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []

for i in li:
    if i % 2 != 0:
        new_list.append(i)

print("After removing evens :",new_list)