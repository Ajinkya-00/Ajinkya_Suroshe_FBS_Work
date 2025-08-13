#  x - x^2/3 + x^3/5 - x^4/7 + ... up to n terms

x = int(input("Enter x: "))
n = int(input("Enter the number of terms: "))
total = 0

for i in range(1, n + 1):
    numerator = x ** i
    denominator = 2 * i - 1   # 1,3,5,7....
    sign = 1 if i % 2 == 1 else -1  # +,-,+,-....
    total = total + (numerator / denominator) * sign
print("Sum =", total)