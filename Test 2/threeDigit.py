num = int(input("Enter the three digit number: "))

temp = num

n1 = temp % 10
temp //= 10

n2 = temp % 10
temp //= 10

n3 = temp % 10

if( n2 * 2 == n3) and (n1 * 0.5 == n3):
    print("Yes you have done it")
else:
    print("Plz try again")