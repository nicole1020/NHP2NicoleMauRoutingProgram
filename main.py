# C950 Data Structures and Algorithms II - NHP2 - Routing Program
from Address import loadaddressdata
from Distance import loaddistancedata
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.
# Ref: zyBooks: zyDE 6.12.1: Dijkstra's shortest path example.
# Ref: Graph Data Structure 4.

from Hash import ChainingHashTable
from Package import loadPackageData
from Truck import Truck, loadingpackages, deliveringpackages

# Hash table instance
packagehashtable = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('Package.csv', packagehashtable)

# 2d lists below
# https://www.pythonpool.com/python-2d-list/
# address list rows (x)

addressdatalist = []

loadaddressdata('Address.csv', addressdatalist)

# distances list column (y)

distancedatalist = []

loaddistancedata('Distance.csv', distancedatalist)


def getPackageData():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(packagehashtable.table) + 1):
        print("PackageID: {}".format(packagehashtable.search(i + 1)))  # 1 to 40 is sent to myHash.search()


# add up total mileage here with KNN alg
# getPackageData()

# edit truck 1 as needed
# instantiated truck objects 1,2, and 3
truck1 = Truck(16, 18, loadingpackages(1, 16, 40, ""), deliveringpackages(1, 800, 40))
truck2 = Truck
truck3 = Truck


# loading trucks algorithm


# https://www.geeksforgeeks.org/sum-manhattan-distances-pairs-points/   logic for complexity
def distanceinbetween(add1, add2):
    distance = 0.0
    add1 = addressdatalist.index(add1)
    add2 = addressdatalist.index(add2)
    for x1, x2 in distancedatalist[add1][add2]:
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return float  # distance


# 9-Return distanceData[addressData.index(address1)][addressData.index(address2)]
#  i.e. distances between addresses can be accessed via distanceData[i][j];
# mindistancefromaddress(address,package) min = 1000, next address #null, next id = 0, returns next address next id,
# minn#distance
def min_distance_from_address(address, package, next_address=None):
    minn = 1000  # distance
    next_address  # null
    next_id = 0
    return next_address, next_id, minn


# delivering_packages(truck, starttime) return miles, calls min_distance_from_address

def delivering_packages(truck, starttime, miles=None):
    return miles


# calls min_distance_from_address
def getPackageDataTime():
    pass


if __name__ == '__main__':
    print("\nWelcome to C950: Routing Program: Hash Table, CSV Import, Greedy Algorithm (Nearest Neighbor), "
          "Dijkstra Algorithm")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Print All Package Status and Total Mileage")
        print("2. Get a Single Package Status with ID")
        print("3. Get Package Status with a Time")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,or 3): ")
        if option == "1":
            getPackageData()
        elif option == "2":
            print("Please enter package ID for more information")
            packageID = input(" ")
            searchresult = packagehashtable.search(int(packageID))
            print(searchresult)

        elif option == "3":
            getPackageDataTime()
        elif option == "4":
            isExit = False
        else:
            print("Invalid option, please try again!")
        # main - END
