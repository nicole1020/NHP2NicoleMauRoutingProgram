# C950 Data Structures and Algorithms II - NHP2 - Routing Program

# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.
# Ref: zyBooks: zyDE 6.12.1: Dijkstra's shortest path example.
# Ref: Graph Data Structure 4.
import csv
from Hash import ChainingHashTable
from Package import Package
from Truck import Truck
import datetime

# Hash table instance
packagehashtable = ChainingHashTable()


def loadPackageData(fileName, packagehashtable):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=",")
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDt = package[5]
            pWeight = package[6]
            pNotes = package[7]
            pStatus = "Unknown"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDt, pWeight, pNotes, pStatus)
            # print(p)

            # insert it into the hash table
            packagehashtable.insert(pID, p)

    return packages


# Load packages to Hash Table
loadPackageData('Package.csv', packagehashtable)
# 2d lists below
# https://www.pythonpool.com/python-2d-list/
# address list rows (x)

addressData = ['4001 South 700 East', '1060 Dalton Ave S', '1330 2100 S', '1488 4800 S', '177 W Price Ave',
               '195 W Oakland Ave', '2010 W 500 S', '2300 Parkway Blvd', '233 Canyon Rd', '2530 S 500 E',
               '2600 Taylorsville Blvd', '2835 Main St', '300 State St', '3060 Lester St', '3148 S 1100 W',
               '3365 S 900 W', '3575 W Valley Central Sta bus Loop', '3595 Main St', '380 W 2880 S', '410 S State St',
               '4300 S 1300 E', '4580 S 2300 E', '5025 State St', '5100 South 2700 West', '5383 South 900 East #104',
               '600 E 900 South', '6351 South 900 East']

# print(addressData[0])
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


# print(distanceData[2][0])


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


# print((distanceinbetween('4001 South 700 East',
#                         '1060 Dalton Ave S', )))

# loading trucks manually
# some packages must be on the same truck, first 2 trucks are for standard deliveries.
# some must go on truck 3 if special instructions given.
# loading truck 1, pid, address, delivery time, weight, special notes
loadtruck1 = list([1, 2, 4, 13, 14, 16, 19, 15, 20, 34, 29, 30, 31, 37, 40, 39])
# print(loadtruck1)

loadtruck2 = list([3, 5, 6, 7, 8, 10, 11, 12, 17, 18, 21, 22, 23, 25, 36, 38])

loadtruck3 = list([9, 24, 26, 27, 28, 32, 33, 35])

# all packages in list on trucks
allpackagesarray = loadtruck1 + loadtruck2 + loadtruck3

# test print all packages in list
# print(allpackagesarray)

starttime1 = '08:00:00'
h, m, s = starttime1.split(':')
timeobject = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
# print(timeobject)

truck1 = Truck('truck1:', 16, 18, loadtruck1, timeobject)
# instantiated truck objects 1,2, and 3
# print(truck1.starttime)
# print(truck1.time)

starttime2 = '09:05:00'
h, m, s = starttime2.split(':')
timeobject = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
# print(timeobject)

truck2 = Truck('truck2:', 16, 18, loadtruck2, timeobject)
starttime3 = '11:00:00'
h, m, s = starttime3.split(':')
timeobject = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
# print(timeobject)

truck3 = Truck('truck3:', 16, 18, loadtruck3, timeobject)


# test print truck


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
# trouble selecting packages from list by address (https://www.tutorialspoint.com/list-methods-in-python-in-not-in-len-min-max)
# https://stackoverflow.com/questions/14588367/update-iteration-value-in-python-for-loop
# https://stackoverflow.com/questions/52875257/nested-for-loop-in-python-doesnt-iterate-fully

# https://gis.stackexchange.com/questions/342586/finding-minimum-distance-from-list-of-coordinates

def mindistancefromaddress(address, packages):
    minn = 1000  # distance
    nextaddress = ''  # null
    nextid = 0

    for pack in packages:
        # take address from hash and find its address id in addressData
        # print(eachaddress)
        package = packagehashtable.search(pack)
        add2 = package.address
        fdistance = distanceinbetween(address, add2)
        print("This is the distance in miles between starting address:", address, "& next address:", add2,
              "with distance in miles:", fdistance)

        if fdistance < minn:
            minn = fdistance
            nextaddress = add2
            nextid = package

        return nextaddress, nextid, minn


mindistancefromaddress('4300 S 1300 E', [3,6,18,25,36,38,5,7,8,10,11,12,17,21,22,23])


# 12/10 work on delivering packages next
# delivering_packages(truck, starttime) return miles, calls min_distance_from_address

def deliveringpackages(truck):
    miles = ''
    nextaddress = ''
    nextid = ''
    minn = ''

    for packs in truck.packages:
        nextaddress, nextid, minn = mindistancefromaddress(truck.currentlocation, truck.packages)
    print(truck)
    # update miles based on distance traveled how many miles left, calculate next address, total distance, total distance traveled
    # next address will be trucks current location, calculate time object to calculate time
    return miles

# deliveringpackages(truck2)

# needs to be at end of day

# alltruck1miles = deliveringpackages(truck1)
# alltruck2miles = deliveringpackages(truck2)
# alltruck3miles = deliveringpackages(truck3)

# currenttruck1miles = deliveringpackages(truck1)
# currenttruck2miles = deliveringpackages(truck2)
# currenttruck3miles = deliveringpackages(truck3)

# truck1milesremaining = alltruck1miles - currenttruck1miles
# truck2milesremaining = alltruck2miles - currenttruck2miles
# truck3milesremaining = alltruck3miles - currenttruck3miles

# totalmiles = currenttruck1miles + currenttruck2miles + currenttruck3miles


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
            #print("\nTotal miles traveled today: ", totalmiles)
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
