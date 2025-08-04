# Convert the time entered in hr ,min and sec into seconds.

hr = int(input("Enter hours: "))
min = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))

total_seconds = (hr * 3600) + (min * 60) + sec

print(f'Total time in seconds: {total_seconds} seconds.')