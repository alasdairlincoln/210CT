#gets the user to enter a number, keeps asking until the user enters a positive integer
user = False
while user == False:
    try:
        parameter = int(input("Please enter a positive integer: "))
        user = True
    except ValueError:
        print("Thats not a positive integer.")

rootParameter = (parameter)**0.5 #finds the root of the input by working out the number to the root of 0.5
perfectSquare = (int(rootParameter))**2 #rounds the rootnumber to a whole number and the squares it
print("The highest perfect square which is less or equal to",parameter,"is",perfectSquare)
