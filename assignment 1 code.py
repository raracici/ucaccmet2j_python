# setting up appropriate data structure
rainfall = {}
with open("stations.csv") as file:
    columns = file.readline()
    for line in file:
        station = line.strip().split(",")
        rainfall[station[0]] = {
            "station": station[2],
            "state": station[1],
            "totalMonthlyPrecipitation": [],
            "relativeMonthlyPrecipitation": [],
            "totalYearlyPrecipitation": 0,
            "relativeYearlyPrecipitation": 0
        }

# importing data from datafile
import json
with open("precipitation.json") as file:
    data = json.load(file)

# defining relevant variables and sorting data per month in Seattle
for i in range(1,13):
    rainfall["Seattle"]["totalMonthlyPrecipitation"].append(0)  # adding 12 values, one per month
for measurement in data:
    if measurement["station"] == rainfall["Seattle"]["station"]:  # islolating data to Seattle
            date = measurement["date"].split("-")  # splitting date key into list
            month = int(date[1])  # calculating month per measurement
            rainfall["Seattle"]["totalMonthlyPrecipitation"][int(month - 1)] += int(measurement["value"]) # adding value into monthly measurement

# saving results for assignment 1
with open("result1.json", "w") as file:
    json.dump(rainfall, file)
