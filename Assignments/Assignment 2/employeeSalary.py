
baseSalary = int(input("Enter the base salary:"))

da = baseSalary  * 0.10
ta = baseSalary  * 0.12
hra = baseSalary * 0.15

FinalSalary = baseSalary + da + ta + hra

print(f'finalsalary : { FinalSalary}')