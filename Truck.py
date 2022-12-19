


class Truck:

    def __init__(self, number, capacity, speed, packages, timeleft):
        self.number = number
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.timeleft = timeleft
        self.time = timeleft
        self.currentlocation = '4001 South 700 East'

    def __str__(self):
        return " %s, %s, %s, %s, %s, %s" % (self.number, self.capacity, self.speed, self.packages, self.timeleft, self.currentlocation)

