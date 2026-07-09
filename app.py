marks = range(1,51)

for mark in marks:
    if (mark % 3 == 0 and mark % 5 == 0):
        print("FizzBuzz")
    elif (mark % 3 == 0):
        print("Fizz")
    elif (mark % 5 == 0):
        print("Buzz")
    else:
        print(mark)