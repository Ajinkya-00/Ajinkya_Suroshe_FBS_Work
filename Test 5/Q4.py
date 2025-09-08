# Number frequency count

def frequency(li):
    freq = {}

    for i in range(len(li)):
        num = li[i]
        count = 0

        for j in range(len(li)):
            if li[j] == num:
                count += 1
        
        freq[num] = count
    return freq

li = [1,3,4,1,2,7,4,8,6,2]
print(frequency(li))