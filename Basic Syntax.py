#It is a combination of c & c++ with indentation, excluding semi colones
#Its an Indented language
#Functional programming language
#Interpeted


print(2+2)


#Input
name = input("Enter your name : ")
print(name)


#if-elif-else
maths = int(input("Enter marks : "))
physics = int(input("Enter marks : "))
chemistry = int(input("Enter marks : "))
english = int(input("Enter marks : "))
computer_science = int(input("Enter marks : "))
ttl = maths+chemistry+physics+english+computer_science
avg = ttl/5
print("Total : ", ttl)
print("Average is",avg)
if(avg<40):
    print("Grade : F")
#avg<60 and 40<avg is a good practice
elif(40<avg<60):
    print("Grade : C")
elif(60<avg<80):
    print("Grade : B")
else : 
    print("Grade : A")


#List
#declaration -> l=[]
#definition -> l=[1,2,3,4,5]
l = [11,33,55,"a","b"]
print(l)

#Forward indexing starts from 0, Backward indexing starts from -1
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

# print(l[-1])
# print(l[-2])
# print(l[-3])
# print(l[-4])
# print(l[-5])


#Append method : object.append(value)
l.append(99)
print(l)


#List slicing is base on index
#Syntax -> First term : Last term : Common difference
print(l[0:5:2])
print(l[0:5])
print(l[1:4])
print(l[2:4])
print(l[:])