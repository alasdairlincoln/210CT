def remove_vowels(string, i, finalArray):
    '''This function takes a string and itterates
    over it removing vowels and outputting the vowelless string'''
    
    vowels = ["a","e","i","o","u"]
    
    if i >= len(string): #base case to stop the recersive function
        finalString = "".join(finalArray) #joins the remaining letters to form a string
        print(finalString)
        return

    else:        
        if string[i] not in vowels:
            finalArray.append(string[i])
        remove_vowels(string, i+1, finalArray)



user = input("Please enter a string: ")
userArray = list(user) #splits the users string into an array of letters
i = 0
finalArray = []
remove_vowels(userArray, i, finalArray)
