# S = a + a^2/2 + a^3/3 + ... + a^10/10

n = int(input("Enter the value of n: "))
total = 0

for i in range(1, 11):
    total += (n ** i) / i
print("Sum =", total)