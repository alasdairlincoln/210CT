def is_prime(n, posdiv):
    '''Function to work out if a number is prime'''
    if n <= 1:
        print("False", n, "isnt a prime number")
        return #A prime number is a natural number thats greater than 1

    elif n <= 3:
        print("True", n,"is a prime number")
        return #2 and 3 are prime numbers so dont need to be checked

    if posdiv == 1: #base case to end the recursivly called function
        print("True", n,"is a prime number")
        return

    if n % posdiv == 0: #works out the modulus of the number divided by 1 less. if it equals 0 it cant be prime
        print("False", n,"isn't a prime number")
        return

    else:
        is_prime(n, posdiv -1)#recursivly calls itself with the divisor being 1 less than last time

entered = False

#gets the user to enter a number, makes sure it is an integer
while entered == False:
    try:
        user = int(input("Enter an integer to check if its prime: "))
        entered = True
    except ValueError:
        print("Please enter an integer")

posdiv = user - 1

is_prime(user,posdiv)
