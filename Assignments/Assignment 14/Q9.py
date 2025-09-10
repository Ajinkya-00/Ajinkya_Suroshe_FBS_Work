# Three numbers with sum = target

def three_sum(num, target):
    result = []

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            for k in range(j+1, len(num)):
                if num[i] + num[j] + num[k] == target:
                    result.append((num[i], num[j], num[k]))
    return result

num = [1,2,3,4,5,6,7]
target = int(input("Enter the target : "))

result = three_sum(num, target)

print(result)