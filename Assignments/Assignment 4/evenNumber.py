# Print all even numbers until n

n = int(input("Enter the number: "))

for num in range(2, n+1, 2):
    if(num % 2 == 0):
        print(num, end=' ')
        