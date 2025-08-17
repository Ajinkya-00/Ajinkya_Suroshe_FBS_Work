# Sum of odd numbers 1 to n

def sum_odd():
    n = int(input("Enter the number: "))
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    
    print("Sum of odd numbers is: ",total)

sum_odd()