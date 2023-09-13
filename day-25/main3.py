import pandas

data = pandas.read_csv("./day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = 0
red = 0
black = 0

for color in data["Primary Fur Color"]:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        red += 1
    elif color == "Black":
        black += 1
    
    
squirrel_colors = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}

squirrel_data = pandas.DataFrame(squirrel_colors)
squirrel_data.to_csv("./day-25/squirrel_count.csv")
