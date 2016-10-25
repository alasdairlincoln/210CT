user = False
while user == False:
    try:
        parameter = int(input("Please enter a positive integer: "))
        user = True
    except ValueError:
        print("Thats not a positive integer.")

rootParameter = (parameter)**0.5
perfectSquare = (int(rootParameter))**2
print("The highest perfect square which is less or equal to",parameter,"is",perfectSquare)
