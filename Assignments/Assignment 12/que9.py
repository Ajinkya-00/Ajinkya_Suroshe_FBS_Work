# Count words and characters

str = input("Enter the string : ")
words = 1
chars = 0

for ch in str:
    chars += 1

    if ch == " ":
        words += 1

print("Words :",words)
print("Characters :",chars)