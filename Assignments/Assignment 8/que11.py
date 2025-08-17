# Armstrong number check

def armstrong():
    num = int(input("Enter a number: "))
    temp = num
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        power = 1
        for i in range(count):
            power *= digit
        total += power
        temp //= 10
    if total == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

armstrong()
