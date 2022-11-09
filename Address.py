import csv


class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return " %s " % self.address


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