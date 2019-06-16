print("\n\n************ Remove Repeated Value from List Program made By Ubaid ************\n\n")

list = [3,4,5,6,7,8,4,3,2,4,9,3]

print("Here is the List : ",end="")
print(list)
print("\n In the List ( Number 3 ) and ( Number 4 ) are Repeated Three times:")

for r in range(3):
    list.remove(3)
    list.remove(4)


print("\n Now, the List after Removing Repeated Values ( Number 3 ) and ( Number 4 ) are : ",end="")
print(list)    


