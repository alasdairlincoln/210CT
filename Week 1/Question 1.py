from random import *

array = []
done = False
print("To finish entering numbers please enter a non integer.")
while done == False:
    try:
        user = int(input("Please enter a number into the array: "))
        array.append(user)

    except ValueError:
        done = True

print("This is the original array of numbers: ",array)
newarray = []
used = []
for i in range(len(array)):
    randin = True
    while randin == True:
        rand = randint(0,(len(array)-1))
        if rand in used:
            randin = True
        else:
            used.append(rand)
            randin = False

    newarray.append(array[rand])

if array == newarray:
    print("Error: List not shuffled, please try again.")

print("This is the shuffled array of numbers",newarray)
