n = 100
size = 10
num = n

for i in range(size):
    row = []
    for j in range(size):
        row.append(num)
        num = num - 1
    
    if i % 2 == 0:
        row = row[::-1]
    
    print(row)