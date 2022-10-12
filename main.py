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
from Greedy import greedyAlgorithmMinTime
from Dijkstra import Vertex, Graph, dijkstra_shortest_path, get_shortest_path, get_shortest_path_city

# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('Packages.csv', myHash)
def getPackageData():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(myHash.table) + 1):
        print("Movie: {}".format(myHash.search(i + 1)))  # 1 to 11 is sent to myHash.search()


getPackageData()

print("\nGreedy Algorithm: Min Expenses => Max Profits")
greedyAlgorithmMinTime(102)  # $102.00 budget
greedyAlgorithmMinTime(94)  # $94.00 budget
greedyAlgorithmMinTime(71)  # $71.00 budget
greedyAlgorithmMinTime(200)  # $200.00 budget

def dijkstraAlgorithmShorthestPath():
    # Dijkstra shortest path main
    # Program to find shortest paths from vertex A.
    g = Graph()

    # add Vertices
    vertex_1 = Vertex("1")  # 1, Western Governors University (Hub), 4001 South 700 East, Salt Lake City, UT, 84107
    g.add_vertex(vertex_1)
    vertex_2 = Vertex("2")  # 2, International Peace Gardens, 1060 Dalton Ave S, 84104
    g.add_vertex(vertex_2)
    vertex_3 = Vertex("3")  # 3,Sugar House Park, 1330 2100 S, 84106
    g.add_vertex(vertex_3)
    vertex_4 = Vertex("4")  # 4, Taylorsville-Bennion Heritage City Gov Off, 1488 4800 S, 84123
    g.add_vertex(vertex_4)
    vertex_5 = Vertex("5")  # 5, Salt Lake City Division of Health Services, 177 W Price Ave, 84115
    g.add_vertex(vertex_5)
    vertex_6 = Vertex("6")  # 6, South Salt Lake Public Works, 195 W Oakland Ave, 84115
    g.add_vertex(vertex_6)
    vertex_7 = Vertex("7")  # 7, Salt Lake City Streets and Sanitation, 2010 W 500 S, 84104
    g.add_vertex(vertex_7)
    vertex_8 = Vertex("8")  # 8, Deker Lake, 2300 Parkway Blvd, 84119
    g.add_vertex(vertex_8)
    vertex_9 = Vertex("9")  # 9 , Salt Lake City Ottinger Hall, 233 Canyon Rd, 84103
    g.add_vertex(vertex_9)
    vertex_10 = Vertex("10")  # 10, Columbus Library, 2530 S 500 E, 84106
    g.add_vertex(vertex_10)
    vertex_11 = Vertex("11")  # 11, Taylorsville City Hall 2600 Taylorsville Blvd, 84118
    g.add_vertex(vertex_11)
    vertex_12 = Vertex("12")  # 12, South Salt Lake Police, 2835 Main St, 84115
    g.add_vertex(vertex_12)
    vertex_13 = Vertex("13")  # 13, Council Hall, 300 State St, 84103
    g.add_vertex(vertex_13)
    vertex_14 = Vertex("14")  # 14, Redwood Park, 3060 Lester St, 84119
    g.add_vertex(vertex_14)
    vertex_15 = Vertex("15")  # 15, Salt Lake County Mental Health, 3148 S 1100 W, 84119
    g.add_vertex(vertex_15)
    vertex_16 = Vertex("16")  # 16, Salt Lake County/United Police Dept, 3365 S 900 W, 84119
    g.add_vertex(vertex_16)
    vertex_17 = Vertex("17")  # 17, West Valley Prosecutor, 3575 W Valley Central Sta bus Loop, 84119
    g.add_vertex(vertex_17)
    vertex_18 = Vertex("18")  # 18, Housing Auth. of Salt Lake County, 3595 Main St, 84115
    g.add_vertex(vertex_18)
    vertex_19 = Vertex("19")  # 19, Utah DMV Administrative Office, 380 W 2880 S, 84115
    g.add_vertex(vertex_19)
    vertex_20 = Vertex("20")  # 20, Third District Juvenile Court, 410 S State St, 84111
    g.add_vertex(vertex_20)
    vertex_21 = Vertex("21")  # 21, Cottonwood Regional Softball Complex, 4300 S 1300 E, 84117
    g.add_vertex(vertex_21)
    vertex_22 = Vertex("22")  # 22, Holiday City Office, 4580 S 2300 E, 84117
    g.add_vertex(vertex_22)
    vertex_23 = Vertex("23")  # 23, Murray City Museum, 5025 State St, 84107
    g.add_vertex(vertex_23)
    vertex_24 = Vertex("24")  # 24, Valley Regional Softball Complex, 5100 South 2700 West, 84118
    g.add_vertex(vertex_24)
    vertex_25 = Vertex("25")  # 25, City Center of Rock Springs, 5383 South 900 East #104, 84117
    g.add_vertex(vertex_25)
    vertex_26 = Vertex("26")  # 26, Rice Terrace Pavilion Park, 600 E 900 South, 84105
    g.add_vertex(vertex_26)
    vertex_27 = Vertex("27")  # 27, Wheeler Historic Farm, 6351 South 900 East, 84121
    g.add_vertex(vertex_27)
    # add Edges
    g.add_undirected_edge(vertex_1, vertex_2, 7.2)  # replace amount miles
    g.add_undirected_edge(vertex_1, vertex_3, 3.8)
    g.add_undirected_edge(vertex_3, vertex_2, 7.1)

    g.add_undirected_edge(vertex_4, vertex_1, 11.0)
    g.add_undirected_edge(vertex_4, vertex_2, 6.4)
    g.add_undirected_edge(vertex_4, vertex_3, 9.2)

    g.add_undirected_edge(vertex_5, vertex_1, 2.2)
    g.add_undirected_edge(vertex_5, vertex_2, 6.0)
    g.add_undirected_edge(vertex_5, vertex_3, 4.4)
    g.add_undirected_edge(vertex_5, vertex_4, 5.6)

    g.add_undirected_edge(vertex_6, vertex_1, 3.5)
    g.add_undirected_edge(vertex_6, vertex_2, 4.8)
    g.add_undirected_edge(vertex_6, vertex_3, 2.8)
    g.add_undirected_edge(vertex_6, vertex_4, 6.9)
    g.add_undirected_edge(vertex_6, vertex_5, 1.9)

    g.add_undirected_edge(vertex_7, vertex_1, 10.9)
    g.add_undirected_edge(vertex_7, vertex_2, 1.6)
    g.add_undirected_edge(vertex_7, vertex_3, 8.6)
    g.add_undirected_edge(vertex_7, vertex_4, 8.6)
    g.add_undirected_edge(vertex_7, vertex_5, 7.9)
    g.add_undirected_edge(vertex_7, vertex_6, 6.3)

    g.add_undirected_edge(vertex_8, vertex_1, 8.6)
    g.add_undirected_edge(vertex_8, vertex_2, 2.8)
    g.add_undirected_edge(vertex_8, vertex_3, 6.3)
    g.add_undirected_edge(vertex_8, vertex_4, 4.0)
    g.add_undirected_edge(vertex_8, vertex_5, 5.1)
    g.add_undirected_edge(vertex_8, vertex_6, 4.3)
    g.add_undirected_edge(vertex_8, vertex_7, 4.0)

    g.add_undirected_edge(vertex_9, vertex_1, 7.6)
    g.add_undirected_edge(vertex_9, vertex_2, 4.8)
    g.add_undirected_edge(vertex_9, vertex_3, 5.3)
    g.add_undirected_edge(vertex_9, vertex_4, 11.1)
    g.add_undirected_edge(vertex_9, vertex_5, 7.5)
    g.add_undirected_edge(vertex_9, vertex_6, 4.5)
    g.add_undirected_edge(vertex_9, vertex_7, 4.2)
    g.add_undirected_edge(vertex_9, vertex_8, 7.7)

    g.add_undirected_edge(vertex_10, vertex_1, 2.8)
    g.add_undirected_edge(vertex_10, vertex_2, 6.3)
    g.add_undirected_edge(vertex_10, vertex_3, 1.6)
    g.add_undirected_edge(vertex_10, vertex_4, 7.3)
    g.add_undirected_edge(vertex_10, vertex_5, 2.6)
    g.add_undirected_edge(vertex_10, vertex_6, 1.5)
    g.add_undirected_edge(vertex_10, vertex_7, 8.0)
    g.add_undirected_edge(vertex_10, vertex_8, 9.3)
    g.add_undirected_edge(vertex_10, vertex_9, 4.8)

    g.add_undirected_edge(vertex_11, vertex_1, 6.4)
    g.add_undirected_edge(vertex_11, vertex_2, 7.3)
    g.add_undirected_edge(vertex_11, vertex_3, 10.4)
    g.add_undirected_edge(vertex_11, vertex_4, 1.0)
    g.add_undirected_edge(vertex_11, vertex_5, 6.5)
    g.add_undirected_edge(vertex_11, vertex_6, 8.7)
    g.add_undirected_edge(vertex_11, vertex_7, 8.6)
    g.add_undirected_edge(vertex_11, vertex_8, 4.6)
    g.add_undirected_edge(vertex_11, vertex_9, 11.9)
    g.add_undirected_edge(vertex_11, vertex_10, 9.4)

    g.add_undirected_edge(vertex_12, vertex_1, 3.2)
    g.add_undirected_edge(vertex_12, vertex_2, 5.3)
    g.add_undirected_edge(vertex_12, vertex_3, 3.0)
    g.add_undirected_edge(vertex_12, vertex_4, 6.4)
    g.add_undirected_edge(vertex_12, vertex_5, 1.5)
    g.add_undirected_edge(vertex_12, vertex_6, 0.8)
    g.add_undirected_edge(vertex_12, vertex_7, 6.9)
    g.add_undirected_edge(vertex_12, vertex_8, 4.8)
    g.add_undirected_edge(vertex_12, vertex_9, 4.7)
    g.add_undirected_edge(vertex_12, vertex_10, 1.1)
    g.add_undirected_edge(vertex_12, vertex_11, 7.3)

    g.add_undirected_edge(vertex_13, vertex_1, 7.6)
    g.add_undirected_edge(vertex_13, vertex_2, 4.8)
    g.add_undirected_edge(vertex_13, vertex_3, 5.3)
    g.add_undirected_edge(vertex_13, vertex_4, 11.1)
    g.add_undirected_edge(vertex_13, vertex_5, 7.5)
    g.add_undirected_edge(vertex_13, vertex_6, 4.5)
    g.add_undirected_edge(vertex_13, vertex_7, 4.2)
    g.add_undirected_edge(vertex_13, vertex_8, 7.7)
    g.add_undirected_edge(vertex_13, vertex_9, 0.6)
    g.add_undirected_edge(vertex_13, vertex_10, 5.1)
    g.add_undirected_edge(vertex_13, vertex_11, 12.0)
    g.add_undirected_edge(vertex_13, vertex_12, 4.7)

    g.add_undirected_edge(vertex_14, vertex_1, 5.2)
    g.add_undirected_edge(vertex_14, vertex_2, 3.0)
    g.add_undirected_edge(vertex_14, vertex_3, 6.5)
    g.add_undirected_edge(vertex_14, vertex_4, 3.9)
    g.add_undirected_edge(vertex_14, vertex_5, 3.2)
    g.add_undirected_edge(vertex_14, vertex_6, 3.9)
    g.add_undirected_edge(vertex_14, vertex_7, 4.2)
    g.add_undirected_edge(vertex_14, vertex_8, 1.6)
    g.add_undirected_edge(vertex_14, vertex_9, 7.6)
    g.add_undirected_edge(vertex_14, vertex_10, 4.6)
    g.add_undirected_edge(vertex_14, vertex_11, 4.9)
    g.add_undirected_edge(vertex_14, vertex_12, 3.5)
    g.add_undirected_edge(vertex_14, vertex_13, 7.3)

    g.add_undirected_edge(vertex_15, vertex_1, 567)
    g.add_undirected_edge(vertex_15, vertex_2, 567)
    g.add_undirected_edge(vertex_15, vertex_3, 567)
    g.add_undirected_edge(vertex_15, vertex_4, 567)
    g.add_undirected_edge(vertex_15, vertex_5, 567)
    g.add_undirected_edge(vertex_15, vertex_6, 567)
    g.add_undirected_edge(vertex_15, vertex_7, 567)
    g.add_undirected_edge(vertex_15, vertex_8, 567)
    g.add_undirected_edge(vertex_15, vertex_9, 567)
    g.add_undirected_edge(vertex_15, vertex_10, 567)
    g.add_undirected_edge(vertex_15, vertex_11, 567)
    g.add_undirected_edge(vertex_15, vertex_12, 567)
    g.add_undirected_edge(vertex_15, vertex_13, 567)
    g.add_undirected_edge(vertex_15, vertex_14, 567)


    g.add_undirected_edge(vertex_16, vertex_1, 453)
    g.add_undirected_edge(vertex_17, vertex_1, 453)
    g.add_undirected_edge(vertex_18, vertex_1, 453)
    g.add_undirected_edge(vertex_19, vertex_1, 453)
    g.add_undirected_edge(vertex_20, vertex_1, 453)
    g.add_undirected_edge(vertex_21, vertex_1, 453)
    g.add_undirected_edge(vertex_22, vertex_1, 453)
    g.add_undirected_edge(vertex_23, vertex_1, 453)
    g.add_undirected_edge(vertex_24, vertex_1, 453)
    g.add_undirected_edge(vertex_25, vertex_1, 453)
    g.add_undirected_edge(vertex_26, vertex_1, 453)
    g.add_undirected_edge(vertex_27, vertex_1, 453)
    g.add_undirected_edge(vertex_1, vertex_10, 453)
    # Run Dijkstra's algorithm first.
    dijkstra_shortest_path(g, vertex_1)

    # Get the vertices by the label for convenience; display shortest path for each vertex
    # from vertex_1.
    print("\nDijkstra shortest path:")
    for v in g.adjacency_list:
        if v.pred_vertex is None and v is not vertex_1:
            print("1 to %s ==> no path exists" % v.label)
        else:
            print("1 to %s ==> %s (total distance: %g)" % (v.label, get_shortest_path(vertex_1, v), v.distance))

    print("\nDijkstra shortest path with Cities:")
    for v in g.adjacency_list:
        myMovie = myHash.search(int(v.label))
        if v.pred_vertex is None and v is not vertex_1:
            print("Salt Lake City to %s ==> no path exists" % myMovie.city)
        else:
            print("Salt Lake City to %s ==> %s (total distance: %g)" % (
            myMovie.city, get_shortest_path_city(vertex_1, v, myHash), v.distance))


dijkstraAlgorithmShorthestPath()
# Dijkstra shortest path - END

# main - START
if __name__ == '__main__':
    print("\nWelcome to C950: Classic Movies: Hash Table, CSV Import, Greedy Algorithm, Dijkstra Algorithm")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Get Movie Data")
        print("2. Run Greedy Algorithm with a Budget")
        print("3. Run Dijkstra Algorithm")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,3 or 4): ")
        if option == "1":
            getPackageData()
        elif option == "2":
            budget = int(input("What is your budget (ex. 150)? "))
            greedyAlgorithmMinTime(budget)
        elif option == "3":
            dijkstraAlgorithmShorthestPath()
        elif option == "4":
            isExit = False
        else:
            print("Wrong option, please try again!")
        # main - END

