# Sort employees by salary

def ssort_by_salary(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-1):
            if data[j][2] > data[j+1][2]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

data = [[101,"Seema",45000],
        [340,"Rajani",13000],
        [210,"Tannu",14000],
        [320,"Suresh",35000]
     ]
sorted_data = ssort_by_salary(data)
for emp in sorted_data:
    print(emp)