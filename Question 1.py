number1 = false
number2 = false
number3 = false
number4 = false

while number1 == false:
    try:
        a = int(input("please enter a number: "))
        number1 = true
    except valueerror:
        print("thats not a number. please enter a whole number: ")
        number1 = false

while number2 == false:
    try:
        b = int(input("please enter a second number: "))
        number2 = true
    except valueerror:
        print("thats not a number. please enter a whole number: ")
        number2 = false

while number3 == false:
    try:
        c = int(input("please enter a third number: "))
        number3 = true
    except valueerror:
        print("thats not a number. please enter a whole number: ")
        number3 = false

while number4 == false:
    try:
        d = int(input("please enter a fourth number: "))
        number4 = true
    except valueerror:
        print("thats not a number. please enter a whole number: ")
        number4 = false

fraction1 = a/b
fraction2 = c/d

if fraction1 > fraction2:
    print(fraction1, "is the larger value")
elif fraction2 > fraction1:
    print(fraction2, "is the larger value")
elif fraction1 == fraction2:
    print("the values are the same")
else:
    print("error, please try again")


