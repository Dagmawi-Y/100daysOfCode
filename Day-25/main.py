# with open("weather-data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
# with open("weather-data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for i in data:
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather-data.csv")
# json_data = data.to_json()
# print(type(data))
# print(data["temp"])
# print(json_data)
# temp = data["temp"]
# temp_list = temp.to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 2))

# mean_temp = temp.mean()
# max_temp = temp.max()
# print(mean_temp)
# print(max_temp)
# temperature = data.temp
# print(temperature)
# print(data[data.temp == max(data.temp)])

squirrel_data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrel_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrel_data_dict)
df.to_csv("squirrel_count.csv")

