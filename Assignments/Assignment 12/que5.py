# Count vowels in a string

str = input("Enter the string : ")
vowels = "aeiouAEIOU"
count = 0

for ch in str:
    if ch in vowels:
        count += 1

print(count)