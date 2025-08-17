# Sum of digits

def sum_of_digits():
    n = int(input("Enter a number: "))
    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    
    print("Sum of digits is:", sum)

sum_of_digits()