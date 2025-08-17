#  Sum 1^1 + 2^2 + ... + n^n

def sum():
    n = int(input("Enter a number: "))
    total = 0

    for i in range(1, n + 1):
        power = 1

        for j in range(1, i + 1):
            power *= i
            total += power
    
    print("Sum =",total)

sum()