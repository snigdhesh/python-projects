import datetime

def getEmployeeSalary(hoursWorked, hourlyPay):
    return hoursWorked * hourlyPay

manasaSalary = getEmployeeSalary(40, 15) #manasa
divyaSalary = getEmployeeSalary(35, 20) #divya

print(f"manasa earned {manasaSalary}")
print(f"Divya earned {divyaSalary}")

def getEmployeeInfo(employeeId):
    if(employeeId == 1001):
        return '{"name": "Manasa", "email": "manasa@gmail.com"}'
    elif(employeeId == 1002):
        return '{"name": "Divya", "email": "divya@gmail.com"}'
    else:
        return 'No user found'


user = getEmployeeInfo(1003)
print(user)


def getSchoolStatus(currentTime):
    if 8 <= currentTime.hour < 18:
        return 'school is open'
    else:
        return 'school is closed'


status = getSchoolStatus(datetime.datetime.now().time())
print(status)