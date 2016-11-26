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

def extract_asc(list):
    #create new list to store the subsequence
    listOfSequence = []
    if len(array) == 0:
        return array
    else:
        for i in range (0,len(array-1)):
            #number = number +1
            #in ascending order i can be equal to i+1
            if array[i] < array [i+1]:
                listOfSequence.append(i)
                array(i) = []
                array(i).append(array[[i]])
                #print largest subsequence (largest list inside your list
                #if two or more of same size that are largest, print them all

array = create_array()
