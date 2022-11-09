# C950 Data Structures and Algorithms II - NHP2 - Routing Program

# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.
# Ref: zyBooks: zyDE 6.12.1: Dijkstra's shortest path example.
# Ref: Graph Data Structure 4.

from Hash import ChainingHashTable
from Package import loadPackageData
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


# main - START
def getTruckData():
    print("Trucks:")


# if user query < load time, at hub, if query < delivery time en route else if = delivered

getTruckData()

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
