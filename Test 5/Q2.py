# Missing coin number

def missing_coin(n,coins):
    for i in range(n):
        count = 0
        for j in range(n):
            if coins[i] == coins[j]:
                count = count + 1
        
        if count % 2 != 0:
            return coins[i]

n = int(input("Enter total coins : ")) - 1
coins = []

for i in range(n):
    coins.append(int(input("Enter coin number : ")))

print("Missing coin number =", missing_coin(n,coins))