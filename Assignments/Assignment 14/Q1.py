# Elements in set1 not in set2

def not_in_second(set1,set2):
    result = []

    for i in range(len(set1)):
        found = False
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                found = True
                break
        if found == False:
            result.append(set1[i])
    return result
    
set1 = [1,2,3,4,5]
set2 = [4,5,6,7]

result = not_in_second(set1,set2)

print(result)