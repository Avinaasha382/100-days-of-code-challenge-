import csv
import pandas 

data = pandas.read_csv("weather_data.csv")
print(data[data["temp"]==12])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
countGray = 0
countRed = 0
countBlack = 0

countGray = countGray + len(data[data["Primary Fur Color"]=="Gray"])
countRed = countRed + len(data[data["Primary Fur Color"]=="Cinnamon"])
countBlack = countBlack + len(data[data["Primary Fur Color"]=="Black"])

data_dict = {"Fur color":["grey","red","black"],"count":[countGray,countRed,countBlack]}
newData = pandas.DataFrame(data_dict)
newData.to_csv("squirell_count.csv")


print(data)





    