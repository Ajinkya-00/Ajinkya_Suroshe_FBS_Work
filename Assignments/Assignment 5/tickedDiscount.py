# Ticket Discount based on Age

passengers = int(input("Enter the number of passengers: "))
ticket_price = int(input("Enter ticket price: "))

total_amount = 0

for i in range(1, passengers + 1):
    age = int(input(f"Enter the age of passenger {i}: "))

    if age < 12:
        price = ticket_price * 0.7   # 30% off
    
    elif age >= 59:
        price = ticket_price * 0.5   # 50% off

    else:
        price = ticket_price
    
    print("Passenger", i, "ticket price is: ", price)

    total_amount += price

print("Total amount to be paid is: ", total_amount)