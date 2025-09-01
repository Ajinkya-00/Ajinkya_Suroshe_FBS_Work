li = [50, 55, 25, 80, 64, 10]

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for i  in li:
    if i % m == 0 and i % n == 0:
        print(i, end =' ')