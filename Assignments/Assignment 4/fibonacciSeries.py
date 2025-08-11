# Fibonacci series up to n terms

n = int(input("Enter the number: "))
a = 0
b = 1
count = 0

while(count < n):
    print(a, end='  ')
    a, b = b , a + b
    count += 1

# Using for loop
# n = int(input("Enter terms: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b    