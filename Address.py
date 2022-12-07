import csv


@staticmethod
class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return " %s " % self.address


# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
# https://www.jquery-az.com/7-examples-python-open-read-write-files-io-file-operations/


addressData = [
    '4001 South 700 East',
    '1060 dalton ave s'
]

print(addressData[1])
# loadAddressData()
# addressData.append(4, 4)
