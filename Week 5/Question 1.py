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

def extract_asc(List):
    '''Takes a list of integers and splits it up into sublists of max length in ascending order'''
    listOfSequence = [] #creates a list to store the sub lists
    temp = [] #a temporary list to add items to a sublist

    if len(List) == 0:#checks the list isnt empty
        return List
    else:
        for i in range (0,len(List)):

            if i == len(List)-1: #if i is on the last item of the list
                temp.append(List[i]) #used so the last item doesnt get missed off
                listOfSequence.append(temp)#appends the list of items to the list of lists
                return listOfSequence

            else:
                if List[i] <= List [i+1]: #checks that the list is still ascending
                    temp.append(List[i])#adds the number to the temporary list

                else:
                    temp.append(List[i]) #adds the final number to the temporary list
                    listOfSequence.append(temp) #appends the temporary list to the list of sequances
                    temp = []#resets the temporary list to be empty

def find_largest(List):
    '''Takes a list of sub lists and outputs the longest list(s)'''
    highest = len([])
    index = []
    for i in range (0,len(List)):
        if len(List[i]) == highest: #checks the length of the list against the length of the highest list
            index.append(List[i])#if the list is the same length it is append so that both are kept

        elif len(List[i]) > highest:
            highest = len(List[i])#stores the length of the highest list so future lists can be compared
            if index != []:
                index = []#the previously stored list is no longer highest so it is emptied
                index.append(List[i])#the new highest list is then append
            else:
                index.append(List[i])

    print(index)
    return

array = create_array()
find_largest(extract_asc(array))
