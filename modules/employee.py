def getEmployeeSalary(hoursWorked, hourlyPay):
    return hoursWorked * hourlyPay

def getEmployeeInfo(employeeId):
    if(employeeId == 1001):
        return '{"name": "Manasa", "email": "manasa@gmail.com"}'
    elif(employeeId == 1002):
        return '{"name": "Divya", "email": "divya@gmail.com"}'
    else:
        return 'No user found'