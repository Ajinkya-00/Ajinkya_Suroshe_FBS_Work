# Unique words and count

str = "Python is an is language"
li = str.split()

# unique_words = []
unique_words = set()


for word in li:
    if word not in unique_words:
        # unique_words.append(word)
        unique_words.add(word)

print(unique_words)