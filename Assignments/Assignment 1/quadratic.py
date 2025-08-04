a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

sqrt = ((b**2) - (4*a*c))**0.5

res1 = (-b + sqrt) / (2*a)
res2 = (-b - sqrt) / (2*a)

print(f'Roots are {res1} and {res2}.')