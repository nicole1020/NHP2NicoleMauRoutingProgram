import csv
import pandas as pd


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

    dd = pd.DataFrame(d)
    print(dd)


print(loadDistanceData())

# 410 S State St., Salt Lake City, UT 84111
