class Package:

    def __init__(self, id, address, city, state, zip, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        # delivery time
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.delivery_time = None
        self.mileage = 0
        self.time_left = None

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "Package ID %s, %s, %s, %s, %s, deadline %s, time left %s, delivery time %s, %s, %s, %s,status %s " % (
            self.id, self.address, self.city, self.state, self.zip, self.deadline, self.time_left, self.delivery_time, self.mileage,
            self.weight, self.notes, self.status)
