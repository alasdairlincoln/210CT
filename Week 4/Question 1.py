from math import *

def create_array():
    '''A function which asks the user to enter numbers into an array, the user
    can carry on entering numbers as long as they want. All the inputs are checked to
    make sure they are an integer.'''
    array = []
    done = False
    print("Please enter a sorted list of numbers")
    print("To finish entering numbers please enter a non integer.")
    while done == False:
        try:
            user = int(input("Please enter a number into the array: "))
            array.append(user)

        except ValueError:
            done = True
            return array

def sort_array(list):
    if list == []: #Checks if the list is empty
        return []
    else:
        list.sort()
        return list

def binary_search(array, low, high):
    if len(array) == 1:
        mid = array[0]
    else:
        mid = int((len(array)/2))

    if  array:
        print(False, "There is no number inbetween", low, "and", high)
        return



    if low < mid and high > mid or mid == low or mid == high:
        print(True, "There is a number between", low, "and", high)
        return
    elif low < mid and high < mid:
        return binary_search(array[0:mid], low, high)
    elif low > mid and high > mid:
        return binary_search(array[mid:], low, high)
    else:
        print(False, "There is no number inbetween", low, "and", high)
        return

array = create_array()
sortedArray = sort_array(array)

lowAndhigh = False
while lowAndhigh == False:
    low = False
    while low == False:
        try:
            lownumber = int(input("Please enter the lower bound: "))
            low = True

        except ValueError:
            print("Please enter a integer")

    high = False
    while high == False:
        try:
            highnumber = int(input("Please enter the upper bound: "))
            high = True

        except ValueError:
            print("Please enter a integer")

    if lownumber == highnumber or lownumber > highnumber:
        print("Please make sure the lower and upper bounds are entered correctly")
    else:
        lowAndhigh = True

binary_search(sortedArray, lownumber, highnumber)
