# #Importing module numpy as instance np
import numpy as np
import math

#Creating A numpy array using a python list
list1 = [10, 20, 30, 40]
array1 = np.array(list1)
print(array1)

#Printing a list of 0s
array2 = np.zeros(3)
print(array2)

#Creating a n-d array : 2-d
array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array3)

#shape of the array
print(np.shape(array3))


#Creating 3-d array
array4 = np.array([[[1,2],[4,5]],[[6,7],[8,9]]])
print(array4)

#Arithmetic operations in numpy 
#Adding two numpy arrays using + operator
array5 = np.array([1,2,3,4,5])
array6 = np.array([1,1,1,1,1])
result = array5 + array6
print(result)

#Adding two numpy array using add() function
result2 = np.add(array5, array6)
print(result2)

#Subtracting two numpy arrays using - operator
array7 = np.array([1,2,3,4,5])
array8 = np.array([1,1,1,1,1])
result3 = array7 + array8
print(result3)

# #Subtracting two numpy arrays using subtract function
result4 = np.subtract(array7,array8)

#Multiplication of two numpy arrays using * operator
array9 = [2,2,2,2,2]
result4 = array7*array9
print(result4)

#Multiplication of two numpy arrays using multiply function
result5 = np.multiply(array7, array9)
print(result5)

#Division of numpy arrays using / operator
array10 = np.array([4,10,16,20,24])
result6 = array10 / array9
#Print result in float
print(result6)

# #Division of numpy arrays using divide function
result7 = np.divide(array10, array9)
print(result7)

# #Exponential operation in numpy array
result8 = array7**2
print(result8)

# #Exponential operation in numpy array using power function
result9 = np.power(array7, 2)
print(result9)

# #Modulus of two numpy array using mod function
result10 = np.mod(array7, array9)
print(result10)

#Reshaping and resizing array
array11 = np.array([2,4,6,8,10,12,14,16])
#Reshape function takes parameters as (array,(row,column))
reshapedArray = np.reshape(array11,(4,2))

#Transposing an array
trans = np.transpose(reshapedArray)

#Mean, Median, Minimum, Maximum value of a numpy array
mean = np.mean(array7)
median = np.median(array7)
min  = min(array7)
max = max(array7)