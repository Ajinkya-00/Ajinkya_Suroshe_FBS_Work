# Fibonacci series

def fibonacci():
    n = int(input("Enter the number of terms: "))
    a = -1
    b = 1
    
    for i in range(1, n + 1):
        c = a + b
        print(c)
        a = b
        b = c

    print()
    
fibonacci()