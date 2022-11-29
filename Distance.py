import csv


class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return " %s " % self.distance


distanceData = []

with open('Distance.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        distanceData.append(row[0])

print(distanceData)

# 410 S State St., Salt Lake City, UT 84111
