import math
def greedyAlgorithmMinTime(time):
    total = time
    time1 = 0
    time2 = 0
    time3 = 0

    while (time >= 25):
        if time1 > 3: # why 3? 0,1,2,3 will not break so 4 times.
            break
        time1 += 1
        time = time - 25
    while (time >= 10):
        time2 += 1
        time = time - 10
    while (time >= 5):
        time3 += 1
        time = time - 5


    tTotal = time1 + time2 + time3

    # expense calculation
    eDVDs = 1.00 * tTotal # Material cost of DVD: $1.00
    eLabor = 12.00 * (math.ceil(tTotal/10)) # Labor is $12.00 for every 10 DVDs, $24.00 for 11 DVDs
    eShipping = 0.50 * tTotal # Shipping cost is $0.50 per DVD
    eTotal = eDVDs + eLabor + eShipping
    profit = total - eTotal

    print("${:.2f}-Budget, {}-DVDs, ${:.2f}-Expense, ${:.2f}-Profit ==>".format(total,tTotal,eTotal,profit))
    print(" {} x 25 dollar movie = ${:.2f}".format(time1,time1*25.00))
    print(" {} x 10 dollar movie = ${:.2f}".format(time2,time2*10.00))
    print(" {} x 5  dollar movie = ${:.2f}".format(time3,time3*5.00))