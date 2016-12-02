def reverse(string, reverseS):
    '''A function to take an array and remove and print the last
     item in the array it then repeats until the array is empty'''
    if len(string) == 0: #basecase to stop the recursive function
        print(reverseS)
        return
    else:
        reverseS = reverseS + " " + string.pop() #removes the last word from the list of words and adds it on to the rest of the sentance
        return reverse(string, reverseS)#recusrivly calls istself this time string will be one word shorter as its been popped off

user = input("Please enter a string: ")
stringarray = user.split() #spits the users string up and saves each indivual word to a different index in an array
reverseS = "The reverse of your string is:" #sets up the sentance for the words to be added onto
reverse(stringarray, reverseS)
