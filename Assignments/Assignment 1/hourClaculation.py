
sec = int(input("Enter seconds : "))

hour = sec // 3600
minute = sec // 60
second = sec % 60

print(f'{hour}hours, {minute}minutes, {second}seconds')