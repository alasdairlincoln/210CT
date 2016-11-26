def is_prime(n, posdiv):
    if n <= 1:
        print("False", n, "isnt a prime number")
        return #A prime number is a natural number thats greater than 1
    elif n <= 3:
        print("True", n,"is a prime number")
        return #2 and 3 are prime numbers so dont need to be checked

    if posdiv == 1:
        print("True", n,"is a prime number")
        return
    if n % posdiv == 0:
        print("False", n,"isn't a prime number")
        return
    else:
        is_prime(n, posdiv -1)

entered = False

while entered == False:
    try:
        user = int(input("Enter an integer to check if its prime: "))
        entered = True
    except ValueError:
        print("Please enter an integer")

posdiv = user - 1

is_prime(user,posdiv)
