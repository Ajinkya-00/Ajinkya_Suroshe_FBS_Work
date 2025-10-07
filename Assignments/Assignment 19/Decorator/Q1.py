def memo(func):
    cache = {}
    def inner(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return inner

@memo
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(6))
print(factorial(6))