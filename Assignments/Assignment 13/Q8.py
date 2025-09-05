text = input("Enter the text : ")

words = text.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1
    
print(freq)
