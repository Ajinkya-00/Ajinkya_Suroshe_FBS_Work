li = [12, 40, 34, 25, 10]

for i in range(len(li)):
    for j in range(len(li) - 1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

print("Second largest Number :",li[-2])