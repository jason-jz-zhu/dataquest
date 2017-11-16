f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)





# First, import the CSV module
import csv
# Then, open our file in `r` mode
f = open("nfl.csv", "r")
# Use the csv module to read the file, and convert the result
# to a list
nfl = list(csv.reader(f))



import csv

with open("guns.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
