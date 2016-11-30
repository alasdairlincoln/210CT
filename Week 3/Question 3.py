def remove_vowels(string, i, finalArray):
    '''This function takes a string and itterates
    over it removing vowels and outputting the vowelless string'''

    vowels = ["a","e","i","o","u"]

    if i >= len(string): #base case to stop the recersive function
        finalString = "".join(finalArray) #joins the remaining letters to form a string
        print(finalString)
        return

    else:
        if string[i] not in vowels:# checks if the letter of the string is in the list of vowels
            finalArray.append(string[i])# if the letter isnt a vowel then the letter is added to the list of 'safe' values
        remove_vowels(string, i+1, finalArray) #calls the same function with the next letter of the string

user = input("Please enter a string: ")
userArray = list(user) #splits the users string into an array of letters
i = 0
finalArray = []
remove_vowels(userArray, i, finalArray)
