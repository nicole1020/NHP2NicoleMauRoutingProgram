import csv


class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return " %s " % self.distance


def loadDistanceData():
    with open('Distance.csv', newline='') as d:
        reader = csv.reader(d)
        distanceData = list(reader)
        print(distanceData)


print(loadDistanceData())

# 410 S State St., Salt Lake City, UT 84111
