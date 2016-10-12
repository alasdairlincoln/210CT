floatv = False

while floatv == False:
    try:
        floatvalue = float(input("Please enter a float: "))
        floatv = True
    except ValueError:
        print("Thats not a float, please enter a float")

print(floatvalue)