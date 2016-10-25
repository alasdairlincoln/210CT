userinput = False
trailing = 0

while userinput == False:
    try:
        factnumber = int(input("Please enter a factorial number: "))
        userinput = True
    except ValueError:
        print("Please enter a factorial number (don't include the !)")

while factnumber != 0:
    factnumber = factnumber/5
    trailing = trailing + int(factnumber)

print(trailing)
