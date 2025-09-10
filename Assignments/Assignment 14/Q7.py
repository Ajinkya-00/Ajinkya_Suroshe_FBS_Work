# Find missing numbers between two sets.

def missing_num(set1,set2):
    miss2 = []
    miss1 = []

    for i in range(len(set1)):
        found = False
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                found = True
                break
        if found == False:
            miss2.append(set1[i])

    for j in range(len(set2)):
        found = False
        for i in range(len(set1)):
            if set2[j] == set1[i]:
                found = True
                break
        if found == False:
            miss1.append(set2[j])

    return miss2, miss1

set1 = [1,2,3,4,5]
set2 = [3,4,6,7]

miss2, miss1 = missing_num(set1, set2)

print("Missing in set2:", miss2)
print("Missing in set1:", miss1)