class Truck:

    def __init__(self, capacity, speed, load, packages):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages

    def __str__(self):
        return " %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages)


# create truck object with packages array
def loadingpackages(truckid, capacity, miles, packageid):
    return packageid


def deliveringpackages(truck, starttime, miles=None):
    return miles
