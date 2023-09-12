#with open("./day-25/weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

#import csv

#with open("./day-25/weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)
    
import pandas

data = pandas.read_csv("./day-25/weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avarage_temperature = sum(temp_list)/len(temp_list)
print(round(avarage_temperature))