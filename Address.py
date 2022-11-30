import csv


class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return " %s " % self.address


def loadAddressData():
    with open('Address.csv', 'r') as ad:
        reader = csv.reader(ad)
        addressData = list(reader)
        print(addressData)


print(loadAddressData())
