
# with open("weather_data.csv", mode="r") as w_data:
#     content = [name.strip() for name in w_data.readlines()]

#     print(content)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     # List Comprehension
#     temperatures = [int(row[1]) for row in data if row[1].isdigit()]

#     # for row in data:
#     #     if row[1].isdigit():
#     #         temperatures.append(row[1])

#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict["day"])

# Getting the average
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

# # Getting the max
# max_temp = data["temp"].max()
# print(max_temp)

# # Getting data from columns
# print(data["day"])
# print(data.day)

# Getting data from row
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]

# new_temp = (monday.temp[0] * (9 / 5)) + 32
# print(new_temp)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Getting data from the squirrel_data 
data = pandas.read_csv("squirrel_data_nyc.csv")
colors = data["Primary Fur Color"]

new_data = pandas.DataFrame(colors.value_counts())
new_data.to_csv("squirrel_color.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}

df = pandas.DataFrame(dict)
df.to_csv("squirrel_colorrr.csv")