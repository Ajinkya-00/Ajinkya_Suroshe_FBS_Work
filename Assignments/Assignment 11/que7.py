a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersection = []

for i in a:
    if i in b and i not in intersection:
        intersection.append(i)

print("Intersection :",intersection)