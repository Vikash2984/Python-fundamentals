#Creating tuples
MyTuple = ()
print(MyTuple)
#Adding elements
MyTuple = ("Python",2,3,[11,12,13],("A","B","C"))
#Print updated tuple
print(MyTuple[0])
print(MyTuple[1])
print(MyTuple[2])
print(MyTuple[3])
print(MyTuple[0:2])
print(MyTuple[2:])
print(MyTuple[2][1])

#problem challenge
t1 = (1,2,(3,4,(5,6,[7,8],9)))
print(t1[2][2][3])

#List is mutable where as Tuples are immutable
MyTuple[0] = "Java"
MyTuple.pop(0)
MyTuple.sort()
MyTuple.append(5)
print(len(MyTuple))