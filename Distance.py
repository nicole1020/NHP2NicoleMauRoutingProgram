import csv
from csv import reader


class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return " %s " % self.distance


with open('Distance.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    distanceData = list(csv_reader)
    print(distanceData)

# 410 S State St., Salt Lake City, UT 84111
row_number = 3
col_number = 2
value = distanceData[row_number - 1][col_number - 1]
print('Value in cell at 3rd row and 2nd column : ', value)
print(distanceData[2][1])
