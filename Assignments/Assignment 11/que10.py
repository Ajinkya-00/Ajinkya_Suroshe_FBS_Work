li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = []

for i in li:
    if i % 2 != 0:
        res.append(i)
    
print("After removing even numbers :",res)