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

def extract_asc(List):
    '''Takes a list of integers and splits it up into sublists of max length in ascending order'''
    listOfSequence = []
    temp = []
    if len(List) == 0:
        return List
    else:
        for i in range (0,len(List)):

            if i == len(List)-1:
                temp.append(List[i])
                listOfSequence.append(temp)
                return listOfSequence
            else:
                if List[i] <= List [i+1]:
                    temp.append(List[i])

                else:
                    temp.append(List[i])
                    listOfSequence.append(temp)
                    temp = []

def find_largest(List):
    '''Takes a list of sub lists and outputs the longest list(s)'''
    highest = len([])
    index = []
    for i in range (0,len(List)):
        if len(List[i]) == highest:
            index.append(List[i])

        elif len(List[i]) > highest:
            highest = len(List[i])
            if index != []:
                index = []
                index.append(List[i])
            else:
                index.append(List[i])

    print(index)
    return

array = create_array()
find_largest(extract_asc(array))
