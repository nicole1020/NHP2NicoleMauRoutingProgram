# Python3 code to find sum of Manhattan
# distances between all the pairs of
# given points
# https://www.geeksforgeeks.org/sum-manhattan-distances-pairs-points/
# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

from main import distancedatalist

# Example of getting neighbors for an instance
from math import sqrt



# Return the sum of distance of one axis.
def distancesum(arr, n):
    # sorting the array.
    arr.sort()

    # for each point, finding
    # the distance.
    res = 0
    sum = 0
    for i in range(n):
        res += (arr[i] * i - sum)
        sum += arr[i]

    return res


def totaldistancesum(x, y, n):
    return distancesum(x, n) + distancesum(y, n)


# Driven Code
x = distancedatalist
y = distancedatalist
n = len(x)
print("hello", totaldistancesum(x, y, n))

# This code is contributed by "Sharad_Bhardwaj".