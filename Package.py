import csv


class Package:

    def __init__(self, id, address, city, state, zip, dt, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        # delivery time
        self.dt = dt
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.dt, self.weight, self.notes, self.status)


def loadPackageData(fileName, myHash):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDt = package[5]
            pWeight = package[6]
            pNotes = package[7]
            pStatus = "Unknown"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDt, pWeight, pNotes, pStatus)
            # print(p)

            # insert it into the hash table
            myHash.insert(pID, p)



def loadAddressData():
    with open('Address.csv', 'r') as ad:
        reader = csv.reader(ad)
        addressData = list(reader)
        print(addressData)


print(loadAddressData())

# distance_in_between(address1, address2) returns float
def distance_in_between(add1, add2, miles=None):
    return miles


# mindistancefromaddress(address,package) min = 1000, next address #null, next id = 0, returns next address next id, minn#distance
def min_distance_from_address(address, package, next_address=None):
    minn = 1000
    next_address  # null
    next_id = 0
    return next_address, next_id, minn


# delivering_packages(truck, starttime) return miles, calls min_distance_from_address

def delivering_packages(truck, starttime, miles=None):
    return miles
# calls min_distance_from_address
