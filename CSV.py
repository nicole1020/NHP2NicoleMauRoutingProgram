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
            pNotes= package[7]
            pStatus = "loaded"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes, pStatus)
            #print(p)

            # insert it into the hash table
            myHash.insert(pID, p)