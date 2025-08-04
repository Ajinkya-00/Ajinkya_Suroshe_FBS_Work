import random

id = 'ajinkyasuroshe'
Pass = "Ajinkya@123"

user_name = input("Enter Your ID: ")
password = input("Enter Your Password: ")
captcha = random.randint(1111, 9999)

if(user_name == id and password == Pass):
    print(captcha)
    Enter = int(input("Enter the number: "))
    if(captcha == Enter ):
        print("Valid User.")
else:
    print("Invalid user")
