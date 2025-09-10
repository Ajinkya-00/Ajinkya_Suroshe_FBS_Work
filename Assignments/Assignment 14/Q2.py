# Remove intersection of set2 from set1

def remove_common(set1,set2):
    result = []

    for i in range(len(set1)):
        common = False
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                common = True
                break
            if common == False:
                result.append(set1[i])
    return result

set1 = [1,2,3,4,5]
set2 = [3,4,6]

result = remove_common(set1,set2)

print(result)