import datetime
import modules.employee as employee
import modules.school as school

manasaSalary = employee.getEmployeeSalary(40, 15) #manasa
divyaSalary = employee.getEmployeeSalary(35, 20) #divya

print(f"manasa earned {manasaSalary}")
print(f"Divya earned {divyaSalary}")


user = employee.getEmployeeInfo(1002)
print(user)

status = school.getSchoolStatus(datetime.datetime.now().time())
print(status)