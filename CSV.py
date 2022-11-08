import csv


class Package:

    def __init__(self, id, address, city, state, zip, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.status)


class Truck:
    def __init__(self, capacity, speed, load, packages):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages

    def __str__(self):
        return " %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages)


class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return " %s " % self.distance


class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return " %s " % self.address


def loadPackageData(fileName, myHash):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData) # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pNotes = package[7]
            pStatus = "Delivered"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes, pStatus)
            # print(p)

            # insert it into the hash table
            myHash.insert(pID, p)




def loadDistanceData(filename, myHash):
    with open(filename) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        for distance in distanceData:
            dID = int(distance[0])
            dAddress = distance[1]
            dCity = distance[2]
            dState = distance[3]
            dZip = distance[4]

        # distance object
        d = Distance(dID, dAddress, dCity, dState, dZip)


def loadaddressdata(filename, myHash):
    with open(filename) as address:
        addressData = csv.reader(address, delimiter=',')
        for address in addressData:
            aID = int(address[0])
            aAddress = address[1]
            aCity = address[2]
            aState = address[3]
            aZip = address[4]

        # address object

        #a = Address(aID, aAddress, aCity, aState, aZip)

#distanceinbetween(address1, address2)
#mindistancefromaddress(address,package)
#deliveringpackages(truck, starttime)