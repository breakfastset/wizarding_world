class Car:
    """Represent a Car Object"""

    def __init__(self, plate_number, engine_capacity, fuel=100, distance=0):
        """Initialise the plate number, engine capacity, fuel, distance of Car object"""
        self.plate_number = plate_number
        self.engine_capacity = engine_capacity
        self.fuel = fuel
        self.distance = distance

    def drive(self, distance):
        """Drive the car up to the distance depending on amount of fuel"""
        if distance >= self.fuel:  # if distance to be travelled exceeds fuel
            self.distance += self.fuel  # update the distance traveled to the amount of fuel left
            self.fuel = 0
        else:
            self.fuel -= distance
            self.distance += distance

    def __str__(self):
        """Return Details of Car object"""
        message = "Details of the Car: Plate Number is {}, and its Engine cc: {}".format(self.plate_number,
                                                                                         self.engine_capacity)
        return message
