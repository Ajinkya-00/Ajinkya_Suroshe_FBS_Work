# 3a. Sum 1 + 2 + ... + n

def sum():
    n = int(input("Enter the number: "))
    total = 0

    for i in range(1, n + 1):
        total += i
    print("Sum =",total)

sum()
    