# Sum of series up to n

n = int(input("Enter the number: "))
total = 0

for i in range(1, n+1):
    total += i
print("Sum" ,total)