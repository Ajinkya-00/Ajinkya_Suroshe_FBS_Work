# Generate Dictionary {x : x*x} for Numbers 1 to n

def generate_dict(n):
    square_dict = {}

    for x in range(1, n+1):
        square_dict[x] = x*x
    
    return square_dict

n = int(input("Enter the number : "))

result = generate_dict(n)

print(result)