# Numbers in range divisible by a given number

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
divisor = int(input("Enter the divisor: "))

for i in range(start, end+1):
    if i % divisor == 0:
        print(i, end=' ')
