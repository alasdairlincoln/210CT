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
    if array == []:
        return array
    else:
        subarray=[]
        counter = 0
        for i in range(0, (len(array)-1)):
            if array[i] < array[i+1]:
                subarray.append(i)
            else:
                counter = i

        return subarray



        #while array[end-1] <= array[end]:
        #    print("start",array[start],"end", array[end],"i", i)
        #    subarray[i] = array[start:end]
        #    print(subarray)
        #    end = end + 1
#
#            if end > (len(array)-1):
#                return subarray
#
#        start = end
#        end = end + 1
#        i = i + 1

array = create_array()
print(extract_asc(array))
