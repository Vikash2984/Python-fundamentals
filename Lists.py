#CREATING LIST
#String is an array of characters
country = ["Bharat","Bangladesh","China","Russia"]
print(country)


#accessing lists using index
print(country[0])
print(country[1])
print(country[2])
print(country[3])


#Append method in List
country.append("Africa")
#Print updated list
print(country)


#Inserting new element at the specified index
country.insert(2,"Sri Lanka")
#Print updated list
print(country)


#Sorting list using sort method
country.sort()
#Print updated list
print(country)


#Sorted function
a = sorted(country)
#Print updated list
print(a)
#Old main list remains as it is
print(country)


#Updating values in a list
#Overwriting
country[-1] = "Afghanistan"
#Print updated list
print(country)


#Creating new list
numbers = [1,2,3,4,5]
# Print number list
print(numbers)


# Appending new list to country
country.append(numbers)
# Print updated list
print(country)


#Concatination of list
print(country+numbers)


#Extend method
country.extend(numbers)
#Print updated list
print(country)


# removing element using POP method
# pop method takes index as parameter
country.pop(2)
#Print updated list
print(country)


#Reverse method
numbers.reverse()
#Print updated list
print(numbers)


#Check wether an elements is present in a list or not
print(1 in numbers)
print("Pakistan" in country)


#Shallow copy
l = country.copy()
print(l)


#length of list
print(len(country))