# Calculating nearest neighbor for distances for next delivery address and total mileage for the day
# Traveling salesman problem nearest neighbor Python
# https://www.kaggle.com/code/samuelcortinhas/k-nearest-neighbours-knn-from-scratch

import csv
import itertools
import random
import Address
import Distance



# below is NN above is greedy

def all_routs_tsp(addresses):
    """Generate all possible tours of the cities and choose the shortest tour."""
    return shortest_rout_tour(all_routs(addresses))


def shortest_rout_tour(rout_tour):
    """Choose the rout with the minimum rout length."""
    return min(rout_tour, key=rout_length)


all_routs = itertools.permutations


def rout_length(rout):
    "The total of distances between each pair of consecutive cities in the tour."
    return sum(distance(rout[i], rout[i - 1])
               for i in range(len(rout)))


# Addresses are represented as Points, which are represented as complex numbers
Point = complex
Address = Point


def X(point):
    """The x coordinate of a point."""
    return point.real


def Y(point):
    """The y coordinate of a point."""
    return point.imag


def distance(A, B):
    """The distance between two points."""
    return abs(A - B)


{Address(random.randrange(1000), random.randrange(1000)) for c in range(6)}


def Addresses(n, width=900, height=600, seed=40):
    "Make a set of n cities, each with random coordinates within a (width x height) rectangle."
    random.seed(seed * n)
    return frozenset(Address(random.randrange(width), random.randrange(height))
                     for c in range(n))


rout_length(all_routs(Addresses(8)))

Addresses(5)

[Addresses(5) for i in range(3)]

[Addresses(5, seed=i) for i in range(3)]

all_routs_tsp(Addresses(8))


def plot_rout(rout):
    """Plot the cities as circles and the tour as lines between them."""
    plot_lines(list(rout) + [rout[0]])


def plot_lines(points, style='bo-', plt=None):
    """Plot lines to connect a series of points."""
    plt.plot(map(X, points), map(Y, points), style)
    plt.axis('scaled');
    plt.axis('off')


plot_rout(all_routs_tsp(Addresses(8)))


def nearestNeighbor(distance):
    total = distance
    distance1 = 0
    distance2 = 0
    distance3 = 0
    # 1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.

    # 2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.

    # 3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.
    while distance >= 25:
        if distance1 > 3:  # why 3? 0,1,2,3 will not break so 4 times.
            break
        distance1 += 1
        distance = distance - 25
    while distance >= 10:
        distance2 += 1
        distance = distance - 10
    while distance >= 5:
        distance3 += 1
        distance = distance - 5

    # time1,2,3 convert to miles by 18 mph average use times
    # miles calculation
    totalMiles = distance1 + distance2 + distance3

    print("Mileage for current day".format(total, totalMiles))
