text = input("Enter a sentence : ")
words_less_than_5 = [word for word in text.split() if len(word) < 5]
print("Words less than 5 letters :", words_less_than_5)