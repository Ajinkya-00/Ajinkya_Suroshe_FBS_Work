num = int(input("Enter three digit number: "))
temp =num

d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = num % 10


rev_num = (d1 * 100) + (d2 * 10) + d3

if(num == rev_num):
    print("Is a Palindrome Number.")
else:
    print("Is not a Palindrome Number.")

