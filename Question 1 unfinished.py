from random import *

array = [1,2,3,4,5,6]
print(array)
for i in range(len(array)):
    randin = False
    while randin == False:
        rand = randint(min(array),max(array))
        randin = rand in array
    array[i] = rand
    
print(array)

