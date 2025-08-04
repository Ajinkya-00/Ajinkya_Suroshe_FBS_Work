m1 = int(input("Enter the marks m1: "))
m2 = int(input("Enter the marks m2: "))
m3 = int(input("Enter the marks m3: "))
m4 = int(input("Enter the marks m4: "))
m5 = int(input("Enter the marks m5: "))

Sum = m1 + m1 + m3 + m4 + m5
per = (sum/500)*100
print(f'Obtained marks out of 500 is : {Sum}')

if (per > 80 and per < 91):
    print("Grade A")
elif(per > 70 and per < 81 ):
    print("Grade B")
elif(per > 60 and per < 71):
    print("Grade C")
elif(per > 50 and per < 61):
    print("Grade D")
else:
    print("FAIL")