P=float(input("Enter Principal : "))
T=float(input("Enter Time : ")) 
R=float(input("Enter Rate : "))

# Calculate Compound Interest

CI = P * ((1 + R / 100) ** T )-P

print(f'Compound Interest is {CI}.')