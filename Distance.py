import csv
from csv import reader
from os import write


class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return " %s " % self.distance


# https://www.pythonpool.com/python-2d-list/  start here 12/1
# https://www.guru99.com/python-2d-array.html
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
with open('Distance.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    distanceData = list(csv_reader)
    print(*distanceData, sep="\n")

row_number = 3
col_number = 2
value = distanceData[row_number - 1][col_number - 1]
print(' Value in cell at 3rd row and 2nd column : ', value)
print(distanceData[2][1])


# distanceData.append(4, 4)


def loaddistancedata():
    with open('Distance.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        distanceData = list(csv_reader)
        print(*distanceData, sep="\n")

# https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/
# https://www.guru99.com/python-2d-array.html
# 410 S State St., Salt Lake City, UT 84111
