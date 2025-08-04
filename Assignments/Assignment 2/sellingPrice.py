# Selling Price from Cost Price and Discount

cp = int(input("Enter the cost price: "))
discount = float(input("Enter the discount percentage: "))

sp = cp - (cp * discount / 100)

print(f'Selling price {sp}.')