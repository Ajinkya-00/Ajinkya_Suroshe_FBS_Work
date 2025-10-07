sentence = input("Enter a sentence : ")
word_len = {word: len(word) for word in sentence.split()}
print("Words lengths :", word_len)