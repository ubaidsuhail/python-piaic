print("\n\n************ Print Table Made By Ubaid ************\n\n")

number = int(input("Enter number to print Table : "))
print("")
for z in range(1,11):
    print("\t" + str(number) + " x " + str(z) + " = " + str(number * z))