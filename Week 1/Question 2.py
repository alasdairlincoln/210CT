userinput = False
trailing = 0

#while loop to get the user to input a number, it keeps repeating until the user enters a usable number
while userinput == False:
    try:
        factnumber = int(input("Please enter a factorial number: "))
        userinput = True
    except ValueError:
        print("Please enter a factorial number (don't include the !)")

#while loop to keep dividing the factnumber until its 1 or less
while factnumber >= 1 :
    factnumber = factnumber/5
    trailing = trailing + int(factnumber) #adds the remaining whole part of the factorial onto the trailing number

print(trailing)
