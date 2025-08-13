basic_salary = float(input("Enter the base salary: "))
salary = 20000

if (basic_salary < salary):
    da = basic_salary * 0.10
    ta =  basic_salary * 0.12
    hra = basic_salary * 0.15

else:
    da = basic_salary * 0.15
    ta =  basic_salary * 0.18
    hra = basic_salary * 0.20
   

emp_salary = salary + da + ta + hra
print("Salary:", emp_salary)