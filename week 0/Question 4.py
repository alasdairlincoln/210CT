userstring = input("Please enter a string: ")

bpos = False

while bpos == False:
    try:
        beginingpos = int(input("Please specify the starting position: "))
        bpos = True
    except ValueError:
        print("Thats not a number, please enter a whole number")

len = False

while len == False:
    try:
        length = int(input("Please specify the length: "))
        len = True
    except ValueError:
        print("Thats not a number, please enter a whole numeber")

print(userstring.replace(userstring[beginingpos:(beginingpos+length)],""))
