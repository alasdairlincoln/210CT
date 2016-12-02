def reverse(string, reverseS):
    '''A function to take an array and remove and print the last
     item in the array it then repeats until the array is empty'''
    if len(string) == 0:
        print(reverseS)
        return
    else:
        reverseS = reverseS + " " + string.pop()
        return reverse(string, reverseS)

user = input("Please enter a string: ")
stringarray = user.split() #spits the users string up and saves each indivual word to a different index in an array
reverseS = "The reverse of your string is:"
reverse(stringarray, reverseS)
