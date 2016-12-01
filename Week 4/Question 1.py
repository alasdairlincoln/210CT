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
            done = True
            return array

        except ValueError:
            pass

def sort_array(list):
    '''Simply sorts the entered list to make sure it is sorted before
    being passed into the binary serch function'''
    if list == []: #Checks if the list is empty
        return []
    else:
        list.sort()
        return list

def binary_search(array, low, high):
    '''Takes an array of integers and an interval. Searches through the array using
    the binary search method to find if a number is between the interval'''
    length = len(array)

    if length == 1:
        mid = array[0]
    else:
        mid = int((length)/2)

    if high < array[0] or low > array[length -1]: #prints false because interval is outside of list
        print(False, "There is no number between", low, "and", high)
        return

    else:
        if low <= array[mid] and high >= array[mid]:#works out if the interval is either side of the midpoint
            for i in range (low , high):#iterates over the interval to see id there is a number in the array
                if i in array:
                    print(True, "There is a number between",low, "and", high)
                    return
                else:
                    pass
            print(False, "There is no number between",low, "and", high)

        elif low < mid and high < mid:#works out if the interval is lower than the mid point and calls the function with the lower half of the list
            return binary_search(array[0:mid], low, high)

        elif low > mid and high > mid:#works out if the interval is higher than the mid point and calls the function with the higher half of the list
            return binary_search(array[mid:], low, high)

        else:
            print(False, "There is no number between",low, "and",high)

def lowAndhighInput():
    '''Function to get the user to enter a lower and higher bound. The user must
    enter an integer for both and the 2 numbers must not be equal or the the low
    number be higher than the high number (vice versa)'''
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
            return lownumber, highnumber

array = create_array()
sortedArray = sort_array(array)
lownumber, highnumber = lowAndhighInput()
binary_search(sortedArray, lownumber, highnumber)
