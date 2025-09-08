# Minimum number of notes

def minimun_notes(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5]
    total = 0
    
    for n in notes:
        if amount >= n:
            count = amount // n
            amount = amount - (count * n)
            total = total + count
            print(n,"x",count)
            
    return total

amount = int(input("Enter the amount : "))
print("Minimum notes =", minimun_notes(amount))