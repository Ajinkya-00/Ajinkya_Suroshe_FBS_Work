# N + N^2 + N^3 + ... + N^N

n = int(input("Enter N exponent: "))
total = 0

for i in range(1, n + 1):
    print(i)
    total += n ** i
print("Sum =",total)
