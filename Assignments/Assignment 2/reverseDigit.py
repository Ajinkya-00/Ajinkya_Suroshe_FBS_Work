# Reverse a Three-Digit Number

num = int(input("Enter the three digit no : "))

a = num % 10
b = (num // 10) % 10
c = num // 100

rev = a * 100 + b * 10 + c
print(f'The reverse of {num} is {rev}.')