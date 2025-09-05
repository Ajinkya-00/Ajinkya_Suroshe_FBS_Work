# Swap first and last characters

str = input("Enter any string : ")

new_str = str[-1] + str[1:-1] + str[0]

print(new_str)