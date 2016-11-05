#setting up variables
from random import *
array = []
done = False
newarray = []
used = []

print("To finish entering numbers please enter a non integer.") #used to help the user

#a while loop to get the user to enter numbers into the array, the input is also validated to make sure its usable
while done == False:
    try:
        user = int(input("Please enter a number into the array: "))
        array.append(user)
    except ValueError:
        done = True

print("This is the original array of numbers: ",array) #outputs the users inputted array so they can compare it to the final output

#a for loop that itterates over the array
for i in range(len(array)):
    randin = True
    while randin == True:
        rand = randint(0,(len(array)-1))#picks a random number between 0 and the last index in the array (i.e picks a random index from the array)
        if rand in used:#checks to see if the random index has already been used, if it has then the code will return to the top of the while loop
            randin = True
        else:#if the random index hasnt been used before then it is added to the array of used items (to make sure its not used again), the while loop is then exited
            used.append(rand)
            randin = False
    newarray.append(array[rand])#the item in randomly choosen index is then added to a new array

#checks to see if the array was actually shuffled and lets the user know the program failed
if array == newarray:
    print("Error: List not shuffled, please try again.")

print("This is the shuffled array of numbers",newarray) #outputs the end result
