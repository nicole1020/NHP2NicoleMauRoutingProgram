# NHP2NicoleMauRoutingProgram







C950 WGUPS Algorithm Overview



Date: 12.20.2022

C950 Data Structures and Algorithms II
 
Introduction
This program is to help Western Governors University Parcel Service (WGUPS) track and deliver their packages day by day as they currently are not delivering before the delivery deadline. The requirements include: under 140 miles traveled total, 40 packages, 3 trucks (2 drivers). We are given the necessary distance, package, and address data to organize and prioritize deliveries. From this we are asked to create a program to assist a small and growing company with organization and implementation of a package delivery system.
A. Algorithm Identification
The self-adjusting algorithm I used was K-Nearest Neighbor (NN) algorithm. I utilized the article “Develop k-Nearest Neighbors in Python From Scratch” by Jason Brownlee to write my NN algorithm. Instead of Euclidean distance like provided in the example in the article I used simple distanceinbetween (add1,add2) which called an array of all distances between all calling address1 and address2 and comparing to distance list as distance1 and distance2 and the smallest distance is returned. This is done by a selection sort (time complexity O(n^2)). Then I called distance in between in function mindistancefromaddress (address, packages) which takes the current address and all packages from the hash table to find the closest package address(nextaddress). It returns package next package ID(nextid), and minn distance. Then deliveringpackages(truck) on each truck calls mindistancefromaddress and loops through to track mileage and packages that are delivered. 
Here are some constraints we followed:
1.	Package.csv, Distances, and Address data was loaded.
2.	Trucks were manually loaded with a truck1 and truck2 having 16 packages each and truck3 carrying 8. Truck3 carried the packages with special instructions and latest delivery times.
3.	 Each truck leaves the hub at their time_to_leave (no earlier than 8:00 AM).
Here is the pseudocode for the algorithm.
K-NN
Selection sort O(n^2):
def distanceinbetween(add1, add2):
    vReturn = 0
    h = addressData.index(add1)
    j = addressData.index(add2)
    if h == -1 or j == -1:
        print("BAD", add1, add2)
    if j > h:
        #   if distanceData[h][j] == '':
        vReturn = distanceData[j][h]
    else:
        vReturn = distanceData[h][j]
    return float(vReturn)
O(n^3) 
def mindistancefromaddress(address, packages):
    minn = 1000  # distance
    nextaddress = ''  # null
    nextid = ''

    for pack in packages:
        # take address from hash and find its address id in addressData
        # print(eachaddress
        package = packagehashtable.search(pack)
        if address != package.address:
            fdistance = distanceinbetween(address, package.address)
            #   print("This is the distance in miles between", address, "&", add2,
            #          "with distance in miles:", fdistance)
            #   print(pack)
            if fdistance < minn:
                minn = fdistance
                nextaddress = package.address
                nextid = package.id
    if minn == 1000:
        print("MINN", address, nextaddress, packages)

    return nextaddress, nextid, minn
O(n^2) 
# delivering_packages(truck, starttime) return miles, calls min_distance_from_address
def deliveringpackages(truck):
    miles = 0
    next_address = ''
    nextid = ''
    minn = ''
    current_truck_time = truck.timeleft
    current_address = addressData[0]

    for packageID in truck.packages:
        package_found = packagehashtable.search(packageID)
        package_found.time_left = truck.timeleft
    while len(truck.packages) > 0:
        for packs in truck.packages:
            packageobj = packagehashtable.search(packs)
            #        if packageobj.address != current_address:

            if len(truck.packages) > 1:
                next_address, nextid, minn = mindistancefromaddress(current_address, truck.packages)

            # print(truck) update miles based on distance traveled how many miles left, calculate next address,
            # total distance, total distance traveled next address will be trucks current location, calculate time
            # object to calculate time 18MPH.
            current_truck_time += timedelta(hours=minn / 18)
            packageobj.delivery_time = current_truck_time
            packageobj.status = "Delivered"
            packageobj.mileage = minn
            current_address = next_address
            truck.packages.remove(packageobj.id)
            miles += minn
    return miles

B1. Logic Comments
In this program there are manually loaded trucks. I instantiated truck objects truck1, truck2, and truck3 and loaded packages in a list by loadtruck1 loadtruck2 and loadtruck3 lists. Truck 3 leaves after truck 1 driver returns and truck3 leaves station at 10:22AM. I decided to manually select truck3 packages first because those needed to be delivered late. Truck2 packages needed to be grouped together and truck1 packages had the earliest delivery deadline.
Function distanceinbetween calls between 2 points from current address and next addresses and returns the smallest distance (float). Next I instantiated 3 trucks. Then I call distance in between within mindistancefromaddress making sure to code in so the current address is ignored as an option for next address. We take the values minn, nextid, and nextaddress and call mindistancefromaddress in deliveringpackages. We are then able to hash through packages and deliver packages based on shortest distance and based on packages physically on each truck to deliver them. We calculate miles from the speed and distance (division) and set the status to delivered in the Package.csv file. We keep track of the miles through each iteration. 

B2. Development Environment
I used my Windows 10 pro desktop computer with an Intel(R) Core(TM) i7-2600K CPU @ 3.40GHz   3.40 GHz processor, 8 GB of RAM and PyCharm (Community Edition 2022.2.3) to develop this program.
B3. Space-Time and Big-O
Each function has the complexity of O(n^2).  The overall function has worst case runtime of O(n^2) as each major function (distanceinbetween-selectionsort, mindistancefromaddress, and deliveringpackages) individually has O(n^2) time complexity. 
B4. Scalability and Adaptability
  Since the worst-case scenario for the current program is O(n^2) for increase size and scale it would not be the best long term. Larger data sets (in the trillions) would take an eternity to compile thus not a realistic choice for larger data sets.
B5. Software Efficiency and Maintainability
For current needs of the WGUPS it is relatively easy to input new package, address, and/or distance data every day and to maintain the current program needs relatively minimal effort.


B6. Self-Adjusting Data Structures
In the textbook C950: Data Structures and Algorithms II by Leysecky, in figure 7.2 the chaining hash table has O(n) time complexity itself. The data is linked by chaining and is efficient to retrieve. In the article “What is Chaining in Hash Tables” it states “Hash insertion always occurs in O(1): therefore it is suited for large or growing data sets. To paraphrase the same article also states chaining hash tables can continue to grow as long as there is memory capacity for it. 
C. Original Code

C1. Identification Information
 C2. Process and Flow Comments
Please see NicoleMauRoutingProgram, example of comments here are the trucks initialized and packages loaded. 
 

D. Data Structure
I used the Chaining hash table like in figure 7.2 in the textbook by Lysecky. It links the data and has O(1) time complexity to insert and an O(n) time complexity to remove and search(“What is Chaining in Hash Tables”). This enables quick and efficient retrieval of package data from Packages.csv. 
D1. Explanation of Data Structure
To keep track of ID, Address, City, State, Zip, Deadline, Weight, Notes, Status for each package I used the Chaining hash table like in figure 7.2 in the textbook by Lysecky.In my code I called it packagehashtable. It links the data and has O(1) time complexity to insert and an O(n) time complexity to remove and search(“What is Chaining in Hash Tables”). This enables quick and efficient retrieval of package data from Packages.csv. 
E. Hash Table
To keep track of ID, Address, City, State, Zip, Deadline, Weight, Notes, Status for each package I used the Chaining hash table like in figure 7.2 in the textbook by Lysecky. In my code I called it packagehashtable.  It links the data and has O(1) time complexity to insert and an O(n) time complexity to remove and search(“What is Chaining in Hash Tables”). This enables quick and efficient retrieval of package data from Packages.csv. 
 
F. Look-Up Function
 
In this you’ll see the search(self,key) function within my ChainingHashTable to search the hash for a named key. It can search for any of the package properties (packageID, Address, City, State, Zip, Deadline, Weight, Notes, or Status). 


G. Interface
 
 
G1. First Status Check
Provide screenshots to show the status of allpackages at a time between 8:35 a.m. and 9:25 a.m.
 
 
G2. Second Status Check
Provide screenshots to show the status of allpackages at a time between 9:35 a.m. and 10:25 a.m.
 
 
G3. Third Status Check
Provide screenshots to show the status of allpackages at a time between 12:03 p.m. and 1:12 p.m.
 
 
H. Screenshots of Code Execution
The total mileage traveled by all trucks is displayed under the title heading in the output window. 
 
I1. Strengths of Chosen Algorithm
In the article by Brownlee, the strength of the algorithm is it’s ability to analyze data automatically. To write the code was much easier than graph theory algorithms (Dijkstra’s and Floyds) and is easy to adjusting as data changes.
I2. Verification of Algorithm
The NN algorithm I coded has under 140 miles total traveled and displays in the UI as directed. It is within constraints of WGUPS and finds the shortest distance to the next package for each truck. The packages that needed to be grouped together were delivered on truck 2, other delays and specifications, and package 9 address being updated at 10:20 was properly delivered at 10:30.
I3. Other possible Algorithms
Dijkstras and Greedy Algorithms are two other possible algorithms to implement. Both require graph structures and would need almost 200 vertices combinations hardcoded in. Each time a new address would be added to the list, a new set of combinations would need to be included. Currently 14^2 or 196 combinations. Adding one more address would need another 29 vertex combinations added to the array. Dijkstras calculates edge weights and finds the shortest path figure 6.11.1 (Lysecky) According to the article “Comparison of Dijkstra’s algorithm and Floyd–Warshall algorithm” by Selman Alpdundar, Floyd algorithm uses graph theory and weighted edges and all combinations of vertices. 

I3A. Algorithm Differences
Similar to KNN that we utilized, Dijkstra’s algorithm has time complexity O(n^2) but Floyd-Warshall has a O(n^3) complexity. The discrepancy is because Floyd searches for each vertex (possible address) and each weighted edge(possible next address) while KNN and Dijkstra’s focuses on the current address and which to travel to next. Dijkstra’s and Floyds use graph theory as explained above and have exponentially more datapoints to insert with just 1 change of distance, address or package.

J. Different Approach
If I were to change my code, I would make sure to keep a text log of all deliveries, so I didn’t have to keep running the program for functionality and record keeping for the development process. I believe long term that would bog down a system with increased memory use so it would only be to test the code.
K1. Verification of Data Structure
Option 1 in my CLI provides the printout of all packages in the hash table, thus fulfilling the requirements of the data structure. I added mileage as well to show how far the truck traveled to deliver each package from the previous address.
 
 
K1A. Efficiency
The time complexity for the chaining hash table lookup function(search) is O(n) so with increased package numbers the time is directly dependent. The larger the dataset the longer it takes to search.
K1B. Overhead
The space usage grows as the hash table grows. It will grow infinitely if there is an infinite space in storage. Therefore the size of the hash table is limited by storage space available per article “What is Chaining in Hash Tables.”.
K1C. Implications
The time complexity for the chaining hash table lookup function(search) is O(n) so with increased truck numbers the time is directly dependent. The larger the dataset the longer it takes to search.
K2. Other Data Structures
Two other data structures I could have used are graphs and stacks. Graphs utilized in this scenario would be exponentially more work as the data changes or grows. Each distance point would have to be cross referenced. Stacks would be an easy way to retrieve data with simple commands, but the search function would be not as easy to utilize. The key value pairs make it easy to search in our chaining hash table. 
K2a. Data Structure Differences
Stacks and Graphs have their weaknesses in dynamic programing environment. Graphs utilize only numerical values and stacks are functional only to a point(like a stack of books the data is tough to navigate). Chaining hash tables allow for dynamic access, update, and searching. 
M. Professional Communication
Thank you for taking the time to review this document.


L. Sources - Works Cited
Alpdundar, Selman. “Comparison of Dijkstra’s algorithm and Floyd–Warshall algorithm.” Selman Alpdundar, https://www.selmanalpdundar.com/comparison-of-dijkstras-algorithm-and-floyd-warshall-algorithm.html. Accessed 23 Dec. 2022.

Brownlee, Jason. “Develop k-Nearest Neighbors in Python From Scratch.”  Machine Learning Mastery, https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/. Accessed 15 Dec. 2022.

“Floyd Warshall Algorithm DP-16.” Geeks For Geeks, https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/. Accessed 23 Dec. 2022.

Lysecky, Roman and Fahir Vahid. (2018, June). C950: Data Structures and Algorithms II. zyBooks.
Retrieved October 03, 2022, from  https://learn.zybooks.com/zybook/WGUC950AY20182019/

“What is Chaining in Hash Tables.” Educative, https://www.educative.io/answers/what-is-chaining-in-hash-tables. Accessed 23 Dec. 2022.

