# Login with up to 3 tries

correct_id = "Ajinkya"
correct_pass = "12345"
max_attempts = 3

for attempts in range(1, max_attempts + 1):
    user_id = input("Enter your ID: ")
    user_pass = input("Enter your password: ")
    
    if user_id == correct_id and user_pass == correct_pass:
        print("Login Successful")
        break
    else:
        print("Incorrect ID or Password. Attempts left: ", max_attempts - attempts)
else:
    print("Maximum attempts reached . Program terminated.")
