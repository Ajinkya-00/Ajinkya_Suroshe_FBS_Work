#Write a program to accept distance in km and convert it into meters and
#centimeters both.

km = int(input("Accept the distance in km"))

m = km * 1000
cm = km * 10000

print(f'meter is: {m}, centimeter is: {cm}')
