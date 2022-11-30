import csv


class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return " %s " % self.address


#https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
#https://www.jquery-az.com/7-examples-python-open-read-write-files-io-file-operations/
def loadAddressData():
    with open('Address.csv', 'r') as ad:
        reader = csv.reader(ad)
        addressData = list(reader)
        print(*addressData, sep="\n")


print(loadAddressData())
#addressData.append(4, 4)
