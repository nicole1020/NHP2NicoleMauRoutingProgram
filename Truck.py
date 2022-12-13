import csv


class Truck:

    def __init__(self, capacity, speed, packages, timeleft):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.timeleft = timeleft
        self.time = timeleft
        self.currentlocation = '4001 South 700 East'

    def __str__(self):
        return " %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.packages, self.timeleft, self.currentlocation)

    def starttime(self, param):
        pass

    def currentaddress(self, param):
        pass
