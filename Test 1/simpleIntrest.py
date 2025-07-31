# Write a program to calculate simple interest based on Principal, Rate and Time
#(SI = P*R*T/100)

P = int(input("Enter the Principal: "))
T = int(input("Enter the Time: "))
R = int(input("Enter the Rate: "))

SI = P * T * R / 100

print(f'Simple Intrest is: {SI}')
