def reverse_string(name):
    res = ""
    for i in name:
        res = i + res
    print(res)

def calculate_salary(hourlyPay, hoursWorked):
    grossPay = hourlyPay * hoursWorked
    return grossPay - (0.1 * grossPay)