# Armstrong number 

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    
    if total == num:
        print(num, end=' ')
print("are the Armstrong numbers between", start, "and", end)