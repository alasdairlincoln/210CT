userinput = False

while userinput == False:
    try:
        factnumber = int(input("Please enter a factorial number: "))
        userinput = True
    except ValueError:
        print("Please enter a factorial number (don't include the !)")
        
print(factnumber)
