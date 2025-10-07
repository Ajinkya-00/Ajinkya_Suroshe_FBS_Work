div_by_any = [x for x in range(1, 1001) if any(x % y == 0 for y in range(2, 10))]
print(div_by_any)