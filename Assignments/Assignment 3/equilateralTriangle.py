a1 = int(input("Enter first angle: "))
a2 = int(input("Enter second angle: "))
a3 = int(input("Enter third angle: "))
s1 = int(input("Enter the first side: "))
s2 = int(input("Enter the second side: "))
s3 = int(input("Enter the third side: "))


if(a1 == a2 == a3):
    print("Is Equilateral triangle")
elif(a1 == a2 or a2 == a3 or a1 == a3) & (s1 == s2 or s2 == s3 or s1 == s3):
    print("Is Isosceles triangle")
else:
    print("Is Scelene triangle")