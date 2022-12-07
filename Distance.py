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
# distancedata list resources
# distanceData.append(4, 4)

distanceDataTable = [
    '0.0,,,,,,,,,,,,,,,,,,,,,,,,,,'
    '7.2,0.0,,,,,,,,,,,,,,,,,,,,,,,,,'
    ''
]
print(distanceDataTable[1,0])


# https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/
# https://www.guru99.com/python-2d-array.html
# 410 S State St., Salt Lake City, UT 84111


# https://datagy.io/manhattan-distance-python/
# https://datagy.io/manhattan-distance-python/#:~:text=In%20a%20two%2Ddimensional%20space,%2B%20%7Cy2%20%2D%20y1%7C%20.
# using manhattan distance to calculate for accurate results of truck traveled
# distance_in_between(address1, address2) returns float

