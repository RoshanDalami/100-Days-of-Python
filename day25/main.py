# with open("weather_data.csv",mode="r") as data_file:
#    data_list =  data_file.readlines()

# print(data_list)

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if(row[1] == "temp"):
            continue

        temperature.append(int(row[1]))
print(temperature)
