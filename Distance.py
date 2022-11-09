import csv


class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return " %s " % self.distance


def loadDistanceData(filename):
    with open(filename) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        for distance in distanceData:
            dID = int(distance[0])
            dAddress = distance[1]
            dCity = distance[2]
            dState = distance[3]
            dZip = distance[4]

        # distance object
       # d = Distance(dID, dAddress, dCity, dState, dZip)

