a = [3, 1, 7]
b = [2, 6, 4]
c = a + b

for i in range(len(c)):
    for j in range(len(c) - 1):
        if c[j] > c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]

print("Soted Merged List :",c)