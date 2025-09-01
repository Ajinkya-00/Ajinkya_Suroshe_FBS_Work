li = [1, 2, 3, 4, 5]
rev = []

i = len(li) - 1

while i >= 0:
    rev.append(li[i])
    i -= 1

print("Reversed List :",rev)