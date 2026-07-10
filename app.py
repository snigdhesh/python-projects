def calculateSalary(hoursWorked, hourlyPay):
    return hoursWorked * hourlyPay

manasaSalary = calculateSalary(40, 15) #manasa
divyaSalary = calculateSalary(35, 20) #divya

print(f"manasa earned {manasaSalary}")
print(f"Divya earned {divyaSalary}")