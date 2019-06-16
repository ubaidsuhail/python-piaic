print("\n\n************ Prime Number Program Made By Ubaid ************\n\n")

number = int(input("Enter number to check if it is prime or not : "))
prime =  True


if number < 2:
    print("\n" + str(number) + " is not valid input.It is neither Prime Number nor Composite Number.")
else:
    for x in range(2,number):
        if (number % x) == 0:
             prime = False
             break 
           
    if prime:
        print("\n" + str(number) + " is Prime Number!")
    else:
        print("\n" + str(number) + " is not Prime Number. " + str(number) + " is composite Number.")