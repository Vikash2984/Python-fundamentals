import pandas as pd

#Displaying dictionary in python as a Data Frame using pandas
students = {"Name ":["Jerry","Rahul","Ravi"], "Admitted-year":[2020,2021,2022],"Rank":[12,13,1] }
data = pd.DataFrame(students)
print(data)

#Displaying csv files on console using pandas
newData = pd.read_csv('boston_house_prices.csv')
print(newData)

#To read the initial records of a given data set
headData = newData.head(n=2)
print(headData)