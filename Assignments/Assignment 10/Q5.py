li = [10, 20, 30, 40, 50, 60, 20, 30, 20]
num = int(input("Enter the number to find: "))
count = 0

for i in li:
    if(i == num):
        count += 1

if (count > 0):
    print(f'{num} is present, {count} time.')
else:
    print(f'{num} is not present.')