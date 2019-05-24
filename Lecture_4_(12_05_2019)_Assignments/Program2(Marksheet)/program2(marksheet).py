print("\n******************** Student Marksheet **********************************\n")
name = input("Enter your name : ")
rollno = input ("Enter your Roll Number : ")
courseNumber =int(input ("Enter number of courses in which you enrolled: "))

markslist = []
total_marks_obtained = 0
i=1
while(i <=courseNumber):
    coursename = input("\nEnter Course Name : ")
    markslist.append(float(input("Enter marks (out of 100) : ")))
    i+=1
    

for j in range(courseNumber):
    total_marks_obtained += markslist[j] 

print("\n\n")
print("**************************************************************************")
print("\n\tThe marks obtained by ' "+ name + " ' is : "+str(total_marks_obtained))
print("\n\tThe total marks is : " + str((courseNumber*100)))
percentage = (total_marks_obtained/(courseNumber*100))*100
print("\n\t' "+name+" ' Your Percentage is: "+ str(percentage)+"\n")


if(percentage >=90 and percentage <=100):
    print("\tExcellent: ' " + name + " ' Your Grade is 'A+'")
elif(percentage >=80 and percentage <90):
    print("\tVery Good: ' " + name + " ' Your Grade is 'A'")
elif(percentage >=70 and percentage <80):
    print("\tGood: ' " + name + " ' Your Grade is 'B'")
elif(percentage >=60 and percentage <70):
    print("\tPoor: ' " + name + " ' Your Grade is 'C'")
elif(percentage >=50 and percentage <60):
    print("\tVery Poor: ' " + name + " ' Your Grade is 'D'")
elif(percentage < 50):
    print("\tOOPS: ' " + name + " ' You are Fail")
else:
    print("\tInvalid Percentage")    


print("\n**************************************************************************")