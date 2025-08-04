# finding % using top 5 subjects

m1=int(input("Enter marks of sub 1:"))
m2=int(input("Enter marks of sub 2:"))
m3=int(input("Enter marks of sub 3:"))
m4=int(input("Enter marks of sub 4:"))
m5=int(input("Enter marks of sub 5:"))

gain_marks = m1 + m2 + m3 + m4 + m5
percentage = (gain_marks/500)*100
print(f'Percentage is {percentage}%.')