import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_gray_count = len(data[data["Primary Fur Color"]== 'Gray'])
color_red_count = len(data[data["Primary Fur Color"]== 'Cinnamon'])
color_black_count = len(data[data["Primary Fur Color"]== 'Black'])
print(color_gray_count)
print(color_red_count)
print(color_black_count)

data_dict ={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[color_gray_count,color_red_count,color_black_count],
}
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')