li = [[1, 2], [2, 1], [3, 5], [4, 2]]

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i][1] > li[j][1]:
            li[i], li[j] = li[j], li[i]

print("Sorted by second element :",li)