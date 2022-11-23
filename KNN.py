# Calculating nearest neighbor for distances for next delivery address and total mileage for the day
# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
import csv
from math import sqrt


# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance1 = 0.0
    for i in range(len(row1) - 1):
        distance1 += (row1[i] - row2[i]) ** 2
    return sqrt(distance1)


# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


# Test distance function
with open('distance.csv', newline='') as d:
    reader = csv.reader(d)
    datalist = list(reader)
    print(datalist)

neighbors = get_neighbors(datalist, datalist[0], 26)
for neighbor in neighbors:
    print(neighbor)




def kNearestNeighbor(distance):
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
