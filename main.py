# C950 Data Structures and Algorithms II - NHP2 - Routing Program

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

addressData = [
    '4001 South 700 East',
    '1060 Dalton Ave S',
    '1330 2100 S',
    '1488 4800 S',
    '177 W Price Ave',
    '195 W Oakland Ave',
    '2010 W 500 S',
    '2300 Parkway Blvd',
    '233 Canyon Rd',
    '2530 S 500 E',
    '2600 Taylorsville Blvd',
    '2835 Main St',
    '300 State St',
    '3060 Lester St',
    '3148 S 1100 W',
    '3365 S 900 W',
    '3575 W Valley Central Sta bus Loop',
    '3595 Main St',
    '380 W 2880 S',
    '410 S State St',
    '4300 S 1300 E',
    '4580 S 2300 E',
    '5025 State St',
    '5100 South 2700 West',
    '5383 South 900 East #104',
    '600 E 900 South',
    '6351 South 900 East',
]

print(addressData[0])
distanceData = [
    [0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    [7.2, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    [3.8, 7.1, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    [11.0, 6.4, 9.2, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    [2.2, 6.0, 4.4, 5.6, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    [3.5, 4.8, 2.8, 6.9, 1.9, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     ''],
    [8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     ''],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     ''],
    [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     ''],
    [6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     '', ''],
    [3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0, '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     ''],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0, '', '', '', '', '', '', '', '', '', '', '', '',
     '', ''],
    [5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0, '', '', '', '', '', '', '', '', '', '', '',
     '', ''],
    [4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0, '', '', '', '', '', '', '', '', '', '',
     '', ''],
    [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0, '', '', '', '', '', '', '', '', '',
     '', ''],
    [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0, '', '', '', '', '', '', '',
     '', '', ''],
    [2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0, '', '', '', '', '', '',
     '', '', ''],
    [3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6, 0.0, '', '', '', '', '',
     '', '', ''],
    [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0.0, '', '', '',
     '', '', '', ''],
    [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0, '', '',
     '', '', '', ''],
    [3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0, 0.0,
     '', '', '', '', ''],
    [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0.0,
     '', '', '', ''],
    [6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9,
     4.5, 0.0, '', '', ''],
    [2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4,
     1.7, 5.4, 0.0, '', ''],
    [5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9,
     6.8, 10.6, 7.0, 0.0, ''],
    [3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1,
     4.7, 3.1, 7.8, 1.3, 8.3, 0.0],
]
print(distanceData[2][0])


def getPackageData():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(packagehashtable.table) + 1):
        print("PackageID: {}".format(packagehashtable.search(i + 1)))  # 1 to 40 is sent to myHash.search()


# add up total mileage here with KNN alg
# getPackageData()


# 9-Return distanceData[addressData.index(address1)][addressData.index(address2)]
#  i.e. distances between addresses can be accessed via distanceData[i][j];
# https://www.geeksforgeeks.org/sum-manhattan-distances-pairs-points/   logic for complexity
def distanceinbetween(add1, add2):
    vReturn = 0
    h = addressData.index(add1)
    j = addressData.index(add2)
    if distanceData[h][j] == '':
        vReturn = distanceData[j][h]
    else:
        vReturn = distanceData[h][j]
    return float(vReturn)


print((distanceinbetween('4001 South 700 East',
                         '1060 Dalton Ave S', )))

# loading trucks manually
# some packages must be on the same truck, first 2 trucks are for standard deliveries.
# some must go on truck 3 if special instructions given.
# loading truck 1, pid, address, delivery time, weight, special notes
loadtruck1 = [
    [1, '195 W Oakland Ave', 'Salt Lake City', 'UT', 84115, '10:30 AM', 21, ''],
    [2, '2530 S 500 E', 'Salt Lake City', 'UT', 84106, 'EOD', 44, ''],
    [4, '380 W 2880 S', 'Salt Lake City', 'UT', 84115, 'EOD', 4, ''],
    [13, '2010 W 500 S', 'Salt Lake City', 'UT', 84104, '10:30 AM', 2, ''],
    [14, '4300 S 1300 E', 'Millcreek', 'UT', 84117, '10:30 AM', 88, 'Must be delivered with 15 & 19'],
    [15, '4580 S 2300 E', 'Holladay', 'UT', 84117, '9:00 AM', 4, ''],
    [16, '4580 S 2300 E', 'Holladay', 'UT', 84117, '10:30 AM', 88, 'Must be delivered with 13 & 19'],
    [19, '177 W Price Ave', 'Salt Lake City', 'UT', 84115, 'EOD', 37, ''],
    [20, '3595 Main St', 'Salt Lake City', 'UT', 84115, '10:30 AM', 37, 'Must be delivered with 13 & 15'],
    [29, '1330 2100 S', 'Salt Lake City', 'UT', 84106, '10:30 AM', 2, ''],
    [30, '300 State St', 'Salt Lake City', 'UT', 84103, '10:30 AM', 1, ''],
    [31, '3365 S 900 W', 'Salt Lake City', 'UT', 84119, '10:30 AM', 1, ''],
    [34, '4580 S 2300 E', 'Holladay', 'UT', 84117, '10:30 AM', 2, ''],
    [37, '410 S State St', 'Salt Lake City', 'UT', 84111, '10:30 AM', 2, ''],
    [39, '2010 W 500 S', 'Salt Lake City', 'UT', 84104, 'EOD', 9, ''],
    [40, '380 W 2880 S', 'Salt Lake City', 'UT', 84115, '10:30 AM', 45, '']]

print(loadtruck1)

loadtruck2 = [
    [3, '233 Canyon Rd', 'Salt Lake City', 'UT', 84103, 'EOD', 2, 'Can only be on truck 2'],
    [5, '410 S State St', 'Salt Lake City', 'UT', 84111, 'EOD', 5, ''],
    [6, '3060 Lester St', 'West Valley City', 'UT', 84119, '10:30 AM', 88,
     'Delayed on flight---will not arrive to depot until 9:05 am'],
    [7, '1330 2100 S', 'Salt Lake City', 'UT', 84106, 'EOD', 8, ''],
    [8, '300 State St', 'Salt Lake City', 'UT', 84103, 'EOD', 9, ''],
    [10, '600 E 900 South', 'Salt Lake City', 'UT', 84105, 'EOD', 1, ''],
    [11, '2600 Taylorsville Blvd', 'Salt Lake City', 'UT', 84118, 'EOD', 1, ''],
    [12, '3575 W Valley Central Station bus Loop', 'West Valley City', 'UT', 84119, 'EOD', 1, ''],
    [17, '3148 S 1100 W', 'Salt Lake City', 'UT', 84119, 'EOD', 2, ''],
    [18, '1488 4800 S', 'Salt Lake City', 'UT', 84123, 'EOD', 6, 'Can only be on truck 2'],
    [21, '3595 Main St', 'Salt Lake City', 'UT', 84115, 'EOD', 3, ''],
    [22, '6351 South 900 East', 'Murray', 'UT', 84121, 'EOD', 2, ''],
    [23, '5100 South 2700 West', 'Salt Lake City', 'UT', 84118, 'EOD', 5, ''],
    [25, '5383 South 900 East #104', 'Salt Lake City', 'UT', 84117, '10:30 AM', 7,
     'Delayed on flight-will not arrive to depot until 9:05 am'],
    [36, '2300 Parkway Blvd', 'West Valley City', 'UT', 84119, 'EOD', 88, 'Can only be on truck 2'],
    [38, '410 S State St', 'Salt Lake City', 'UT', 84111, 'EOD', 9, 'Can only be on truck 2']
]

loadtruck3 = [[9, '300 State St', 'Salt Lake City', 'UT', 84103, 'EOD', 2, 'Wrong address listed'],
              [24, '5025 State St', 'Murray', 'UT', 84107, 'EOD', 7, ''],
              [26, '5383 South 900 East #104', 'Salt Lake City', 'UT', 84117, 'EOD', 25, ''],
              [27, '1060 Dalton Ave S', 'Salt Lake City', 'UT', 84104, 'EOD', 5, ''],
              [28, '2835 Main St', 'Salt Lake City', 'UT', 84115, 'EOD', 7,
               'Delayed on flight-will not arrive to depot until 9:05 am'],
              [32, '3365 S 900 W', 'Salt Lake City', 'UT', 84119, 'EOD', 1,
               'Delayed on flight-will not arrive to depot until 9:05 am'],
              [33, '2530 S 500 E', 'Salt Lake City', 'UT', 84106, 'EOD', 1, ''],
              [35, '1060 Dalton Ave S', 'Salt Lake City', 'UT', 84104, 'EOD', 88, '']]

# all packages in list on trucks
allpackagesarray = loadtruck1 + loadtruck2 + loadtruck3

# test print all packages in list
print(allpackagesarray)

# instantiated truck objects 1,2, and 3
truck1 = Truck(16, 18, 387, loadtruck1)
truck2 = Truck(16, 18, 237, loadtruck2)
truck3 = Truck(16, 18, 136, loadtruck3)

# test print truck
print(truck2)


# https://stackoverflow.com/questions/30552656/python-traveling-salesman-greedy-algorithm work here next 12/6-7
# C.2) Function to find min distance/address:
# 10-Define minDistanceFrom(fromAddress, truckPackages)
# 11-Return min distance address to fromAddress
#   i.e. call distanceBetween(address1, address2) in a loop for all the addresses in the Truck

# https://stackoverflow.com/questions/56993212/how-to-loop-a-list-without-repeating-the-pair
# mindistancefromaddress(address,package(list)) min = 1000, next address #null, next id = 0, returns next address next id,
# https://stemlounge.com/animated-algorithms-for-the-traveling-salesman-problem/ o(n^2) complexity
# minn#distance NN here. call NN in delivering packages
# deliver next package to the closest address.
def mindistancefromaddress(address, package, nextaddress=None):
    minn = 1000  # distance
    nextaddress = ''  # null
    nextid = 0

    currentaddress = Truck.currentaddress

    i = currentaddress
    j = nextaddress

    for nextaddress in addressData:
        if distanceinbetween(i, j) > 0:
            print('true')
    return nextaddress, nextid, minn


# 12/10 work on delivering packages next
# delivering_packages(truck, starttime) return miles, calls min_distance_from_address

def deliveringpackages(truck, starttime, mindistancefromaddress, miles=None):
    truck = (truck1, truck2, truck3)
    starttime = ('08:00', '09:05', '11:00')
    truck1.starttime('08:00')
    truck2.starttime('9:05')
    truck3.starttime('11:00')
    mindistancefromaddress()
    return miles


print(deliveringpackages)


# calls min_distance_from_address
# user input into CLI will dictate status of package based on time inputted
def getPackageDataTime():
    pass


if __name__ == '__main__':
    print("\nWelcome to C950: Routing Program: Hash Table, CSV Import, Greedy Algorithm (Nearest Neighbor)")

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
