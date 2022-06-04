import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# total_temp = 0
# avg_temp = 0

# max_temp = data["temp"].max()

# print(data[data.temp == max_temp])
monday = data[data.day == "Monday"]
monday_temp = monday.temp 
fh = (monday_temp*1.8) + 32
print(fh)

#create a dataframe from scratch
data_dict = {
    "students" :["roshan","dalami","sunar"],
    "scores" : [85,89,99]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

