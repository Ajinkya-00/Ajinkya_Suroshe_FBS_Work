def palindrome_num():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

gen = palindrome_num()
for _ in range(20):
    print(next(gen), end = ' ')