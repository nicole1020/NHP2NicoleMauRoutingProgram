# C950 Data Structures and Algorithms II - NHP2 - Routing Program

# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.
# Ref: zyBooks: zyDE 6.12.1: Dijkstra's shortest path example.
# Ref: Graph Data Structure 4.
import datetime
from Hash import ChainingHashTable
from Package import loadPackageData
from NearestNeighbor import greedyAlgorithmMinDistance
from Dijkstra import Vertex, Graph, dijkstra_shortest_path, get_shortest_path, get_shortest_path_city

# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('Package.csv', myHash)


def getPackageData():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(myHash.table) + 1):
        print("Packages: {}".format(myHash.search(i + 1)))  # 1 to 40 is sent to myHash.search()


# add up total mileage here with KNN alg
getPackageData()


# main - START

def getPackageDataTime():
    pass


if __name__ == '__main__':
    print("\nWelcome to C950: Routing Program: Hash Table, CSV Import, Greedy Algorithm, Dijkstra Algorithm")

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
            searchresult = myHash.search(int(packageID))
            print(searchresult)

        elif option == "3":
            getPackageDataTime()
        elif option == "4":
            isExit = False
        else:
            print("Invalid option, please try again!")
        # main - END
