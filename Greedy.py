import math
def greedyAlgorithmMinDistances(distance):
    total = distance
    distance1 = 0
    distance2 = 0
    distance3 = 0
#1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.

#2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.

#3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.
    while (distance >= 25):
        if distance1 > 3: # why 3? 0,1,2,3 will not break so 4 times.
            break
        distance1 += 1
        distance = distance - 25
    while (distance >= 10):
        distance2 += 1
        distance = distance - 10
    while (distance >= 5):
        distance3 += 1
        distance = distance - 5


    dTotal = distance1 + distance2 + distance3

    # expense calculation
    eDVDs = 1.00 * dTotal # Material cost of DVD: $1.00
    eLabor = 12.00 * (math.ceil(dTotal/10)) # Labor is $12.00 for every 10 DVDs, $24.00 for 11 DVDs
    eShipping = 0.50 * dTotal # Shipping cost is $0.50 per DVD
    eTotal = eDVDs + eLabor + eShipping
    profit = total - eTotal

    print("${:.2f}-Budget, {}-DVDs, ${:.2f}-Expense, ${:.2f}-Profit ==>".format(total,dTotal,eTotal,profit))
    print(" {} x 25 dollar movie = ${:.2f}".format(distance1,distance1*25.00))
    print(" {} x 10 dollar movie = ${:.2f}".format(distance2,distance2*10.00))
    print(" {} x 5  dollar movie = ${:.2f}".format(distance3,distance3*5.00))