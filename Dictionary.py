#Creating Dictionary
dict = {"A":1,"B":2,"C":3,"D":4}
print(dict)

#Accessing elements using key
print(dict["A"])

#To display keys of a dictionary using keys method
print(dict.keys())

#To display values of a dictionary using values method
print(dict.values())

#Reassigning values to existing keys of a dictionary
dict["D"] = "Me"                   
print(dict)                                        

#Deleting particular key-value pair using del keyword
del dict["A"]                                     
print(dict)

#Length of a Dictionary
print(len(dict))

#checking keys in a dictionary
print("B" in dict)