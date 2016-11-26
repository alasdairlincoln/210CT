number1 = False
number2 = False
number3 = False
number4 = False

while number1 == False:
    try:
        a = int(input("Please enter a number: "))
        number1 = True
    except valueerror:
        print("Thats not a number. Please enter a whole number: ")
        number1 = False

while number2 == False:
    try:
        b = int(input("Please enter a second number: "))
        number2 = True
    except valueerror:
        print("Thats not a number. Please enter a whole number: ")
        number2 = False

while number3 == False:
    try:
        c = int(input("Please enter a third number: "))
        number3 = True
    except valueerror:
        print("Thats not a number. Please enter a whole number: ")
        number3 = False

while number4 == False:
    try:
        d = int(input("Please enter a fourth number: "))
        number4 = True
    except valueerror:
        print("Thats not a number. Please enter a whole number: ")
        number4 = False

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


