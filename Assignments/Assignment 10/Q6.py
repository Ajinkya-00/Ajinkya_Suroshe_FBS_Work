li = [1, 2, 3, 4, 5, 3, 2, 1]
unique = []

for i in li:
    if i not in unique:
        unique.append(i)

print("List without duplicate :",unique)