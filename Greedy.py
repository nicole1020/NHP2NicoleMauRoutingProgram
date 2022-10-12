import math
def greedyAlgorithmMinTime(time):
    total = time
    c25dollar = 0
    c10dollar = 0
    c5dollar = 0
    c1dollar = 0
    while (time >= 25):
        if c25dollar > 3: # why 3? 0,1,2,3 will not break so 4 times.
            break
        c25dollar += 1
        time = time - 25
    while (time >= 10):
        c10dollar += 1
        time = time - 10
    while (time >= 5):
        c5dollar += 1
        time = time - 5
    while (time > 0):
        if c1dollar > 3:
            break
        c1dollar += 1
        time = time - 1

    cDVDs = c25dollar + c10dollar + c5dollar + c1dollar

    # expense calculation
    eDVDs = 1.00 * cDVDs # Material cost of DVD: $1.00
    eLabor = 12.00 * (math.ceil(cDVDs/10)) # Labor is $12.00 for every 10 DVDs, $24.00 for 11 DVDs
    eShipping = 0.50 * cDVDs # Shipping cost is $0.50 per DVD
    eTotal = eDVDs + eLabor + eShipping
    profit = total - eTotal

    print("${:.2f}-Budget, {}-DVDs, ${:.2f}-Expense, ${:.2f}-Profit ==>".format(total,cDVDs,eTotal,profit))
    print(" {} x 25 dollar movie = ${:.2f}".format(c25dollar,c25dollar*25.00))
    print(" {} x 10 dollar movie = ${:.2f}".format(c10dollar,c10dollar*10.00))
    print(" {} x 5  dollar movie = ${:.2f}".format(c5dollar,c5dollar*5.00))
    print(" {} x 1  dollar movie = ${:.2f}".format(c1dollar,c1dollar*1.00))