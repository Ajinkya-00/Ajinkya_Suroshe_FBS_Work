text = input("Enter the string : ")
vowels = "aeiouAEIOU"
no_vowels = ''.join([ch for ch in text if ch not in vowels])
print("String without vowels :", no_vowels)