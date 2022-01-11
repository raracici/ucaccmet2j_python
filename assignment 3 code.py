# setting up appropriate data structure
rainfall = {}
with open("python assignment\stations.csv") as file:
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
totalprecipitation = 0 # for calculating relativeYearlyPrecipitation

# importing data from datafile
import json
with open("python assignment\precipitation.json") as file:
    data = json.load(file)

# creating loop calculating statistics for each location
for location in "Cincinnati", "Seattle", "Maui", "San Diego":
    for i in range(1,13):
        rainfall[location]["totalMonthlyPrecipitation"].append(0)  # adding 12 values, one per month
    for measurement in data:
        if measurement["station"] == rainfall[location]["station"]:  # islolating data to Seattle
                date = measurement["date"].split("-")  # splitting date key into list
                month = int(date[1])  # calculating month per measurement
                rainfall[location]["totalMonthlyPrecipitation"][int(month - 1)] += int(measurement["value"]) # adding value into monthly measurement
                rainfall[location]["totalYearlyPrecipitation"] += measurement["value"]  # calculating annual percipitation
    # relative rain per month
    for measurement in rainfall[location]["totalMonthlyPrecipitation"]:
        rainfall[location]["relativeMonthlyPrecipitation"].append(measurement/rainfall[location]["totalYearlyPrecipitation"])
    totalprecipitation += rainfall[location]["totalYearlyPrecipitation"]
for location in "Cincinnati", "Seattle", "Maui", "San Diego":   
    rainfall[location]["relativeYearlyPrecipitation"] = rainfall[location]["totalYearlyPrecipitation"]/totalprecipitation

# saving results for assignment 3
with open("python assignment/result3.json", "w") as file:
    json.dump(rainfall, file)