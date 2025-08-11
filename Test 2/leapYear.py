yr = int(input("Enter the year: "))

if ( yr % 4 == 0):
    if( yr % 100 == 0):
        if( yr % 400 == 0):
            print("Leap Year")
        else:
            print("NOT a leap year")
    else:
        print("Leap year")
else:
    print("NOT a leap year")