# Calculating nearest neighbor for distances for next delivery address and total mileage for the day
#Traveling salesman problem nearest neighbor Python

import csv
from math import sqrt



def nearestNeighbor(distance):
    total = distance
    distance1 = 0
    distance2 = 0
    distance3 = 0
    # 1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.

    # 2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.

    # 3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.
    while distance >= 25:
        if distance1 > 3:  # why 3? 0,1,2,3 will not break so 4 times.
            break
        distance1 += 1
        distance = distance - 25
    while distance >= 10:
        distance2 += 1
        distance = distance - 10
    while distance >= 5:
        distance3 += 1
        distance = distance - 5

    # time1,2,3 convert to miles by 18 mph average use times
    # miles calculation
    totalMiles = distance1 + distance2 + distance3

    print("Mileage for current day".format(total, totalMiles))
