p1 = int(input("Enter the price of product 1: "))
p2 = int(input("Enter the price of product 2: "))
p3 = int(input("Enter the price of product 3: "))
p4 = int(input("Enter the price of product 4: "))
p5 = int(input("Enter the price of product 5: "))

sum = p1 + p2 + p3 + p4 + p5
gst = sum * (18/100)
total_cost = gst + sum

print(f'The total bill after adding 18% gst is {total_cost}')
