# Concatenate Two Dictionaries Into One

dict1 = {1 :'A',2 :'B'}
dict2 = {3 :'C',4 :'D'}

result = {}

for i in dict1:
    result[i] = dict1[i]

for i in dict2:
    result[i] = dict2[i]

print(result)