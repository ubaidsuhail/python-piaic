print("\n*************************** Calculator performed calculation for Two Numbers ********************************\n")
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
operator = input("Enter Operator (+ , - , * , / , %) : ")
print("\n")

if(operator == '+'):
    print("The Addition of " + str(num1) + " + " + str(num2) + "  is :  " + str(( num1 + num2 )))
elif(operator == '-'):
    print("The Subtraction of " + str(num1) + " - " + str(num2) + "  is :  " + str(( num1 - num2 )))
elif(operator == '*'):
    print("The Multiplication of " + str(num1) + " * " + str(num2) + "  is :  " + str(( num1 * num2 )))
elif(operator == '/'):
    print("The Division of " + str(num1) + " / " + str(num2) + "  is :  " + str(( num1 / num2 )))
elif(operator == '%'):
    print("The Remainder of " + str(num1) + " % " + str(num2) + "  is :  " + str(( num1 % num2 )))
else:
    print("OOPS:The operation could not proceed because you performed (Invalid Operator)")    
