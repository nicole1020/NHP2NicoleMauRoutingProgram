# C950 Data Structures and Algorithms II - NHP2 - Routing Program

# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.
# Ref: zyBooks: zyDE 6.12.1: Dijkstra's shortest path example.
# Ref: Graph Data Structure 4.


'''
Add this file to the project
Packages.csv:
--------------------------
ID, Address, City, State, Zip, Delivery Deadline, Mass(kg), Notes
1,	195 W Oakland Ave,	Salt Lake City,	UT,	84115,	10:30 AM,	21
2,	2530 S 500 E,	Salt Lake City,	UT,	84106,	EOD,	44
3,	233 Canyon Rd,	Salt Lake City,	UT,	84103,	EOD,	2,	Can only be on truck 2
4,	380 W 2880 S,	Salt Lake City,	UT,	84115,	EOD,	4
5,	410 S State St,	Salt Lake City,	UT,	84111,	EOD,	5
6,	3060 Lester St,	West Valley City,	UT,	84119,	10:30 AM,	88,	Delayed on flight---will not arrive to depot until 9:05 am
7,	1330 2100 S,	Salt Lake City,	UT,	84106,	EOD, 8
8,	300 State St,	Salt Lake City,	UT,	84103,	EOD	, 9
9,	300 State St,	Salt Lake City,	UT,	84103,	EOD, 2 ,	Wrong address listed
10,	600 E 900 South,	Salt Lake City,	UT,	84105,	EOD,	1
11,	2600 Taylorsville Blvd,	Salt Lake City,	UT,	84118,	EOD,	1
12,	3575 W Valley Central Station bus Loop,	West Valley City,	UT,	84119,	EOD,	1
13,	2010 W 500 S,	Salt Lake City,	UT,	84104,	10:30 AM,	2
14,	4300 S 1300 E,	Millcreek,	UT,	84117,	10:30 AM,	88,	Must be delivered with 15, 19
15,	4580 S 2300 E,	Holladay,	UT,	84117,	9:00 AM,	4,
16,	4580 S 2300 E,	Holladay,	UT,	84117,	10:30 AM,	88,	Must be delivered with 13, 19
17,	3148 S 1100 W,	Salt Lake City,	UT,	84119,	EOD,	2
18,	1488 4800 S,	Salt Lake City,	UT,	84123,	EOD,	6,	Can only be on truck 2
19,	177 W Price Ave,	Salt Lake City,	UT,	84115,	EOD,	37
20,	3595 Main St,	Salt Lake City,	UT,	84115,	10:30 AM,	37,	Must be delivered with 13, 15
21,	3595 Main St,	Salt Lake City,	UT,	84115,	EOD,	3
22,	6351 South 900 East,	Murray,	UT,	84121,	EOD,	2
23,	5100 South 2700 West,	Salt Lake City,	UT,	84118,	EOD,	5
24,	5025 State St,	Murray,	UT,	84107,	EOD,	7
25,	5383 South 900 East #104,	Salt Lake City,	UT,	84117,	10:30 AM,	7,	Delayed on flight---will not arrive to depot until 9:05 am
26,	5383 South 900 East #104,	Salt Lake City,	UT,	84117,	EOD,	25
27,	1060 Dalton Ave S,	Salt Lake City,	UT,	84104,	EOD,	5
28,	2835 Main St,	Salt Lake City,	UT,	84115,	EOD,	7,	Delayed on flight---will not arrive to depot until 9:05 am
29,	1330 2100 S,	Salt Lake City,	UT,	84106,	10:30 AM,	2
30,	300 State St,	Salt Lake City,	UT,	84103,	10:30 AM,	1
31,	3365 S 900 W,	Salt Lake City,	UT,	84119,	10:30 AM,	1
32,	3365 S 900 W,	Salt Lake City,	UT,	84119,	EOD,	1,	Delayed on flight---will not arrive to depot until 9:05 am
33,	2530 S 500 E,	Salt Lake City,	UT,	84106,	EOD,	1
34,	4580 S 2300 E,	Holladay,	UT,	84117,	10:30 AM,	2
35,	1060 Dalton Ave S,	Salt Lake City,	UT,	84104,	EOD,	88
36,	2300 Parkway Blvd,	West Valley City,	UT,	84119,	EOD,	88,	Can only be on truck 2
37,	410 S State St,	Salt Lake City,	UT,	84111,	10:30 AM,	2
38,	410 S State St,	Salt Lake City,	UT,	84111,	EOD,	9,	Can only be on truck 2
39,	2010 W 500 S,	Salt Lake City,	UT,	84104,	EOD,	9
40,	380 W 2880 S,	Salt Lake City,	UT,	84115,	10:30 AM,	45

--------------------------
'''

# copy commented codes below and create these modules
from Hash import ChainingHashTable
from CSV import loadPackageData
from Greedy import greedyAlgorithmMinDistance
from Dijkstra import Vertex, Graph, dijkstra_shortest_path, get_shortest_path, get_shortest_path_city

# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('Packages.csv', myHash)
def getPackageData():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(myHash.table) + 1):
        print("Packages: {}".format(myHash.search(i + 1)))  # 1 to 40 is sent to myHash.search()


getPackageData()

print("\nGreedy Algorithm: Min Expenses => Max Profits")
greedyAlgorithmMinDistance(102)  # $102.00 budget
greedyAlgorithmMinDistance(94)  # $94.00 budget
greedyAlgorithmMinDistance(71)  # $71.00 budget
greedyAlgorithmMinDistance(200)  # $200.00 budget


# main - START
def getTruckData():
    pass


if __name__ == '__main__':
    print("\nWelcome to C950: Routing Program: Hash Table, CSV Import, Greedy Algorithm, Dijkstra Algorithm")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Get Package Information")
        print("2. Get Truck Information")
        print("3. Exit the Program")
        option = input("Chose an option (1,2,or 3): ")
        if option == "1":
            getPackageData()
        elif option == "2":
            getTruckData()
        elif option == "3":
            isExit = False
        else:
            print("Invalid option, please try again!")
        # main - END

