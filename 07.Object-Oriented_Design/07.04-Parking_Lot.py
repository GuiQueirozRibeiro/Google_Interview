'''
7.4 Parking Lot: Design a parking lot using object-oriented principles.
'''

from random import randrange

class Vehicle:
    types = []

    def __init__(self, model, size, number):
        self.model = model
        self.size = size
        self.number = number
        self.parked = False

    def is_parked(self):
        if self.parked:
            print("Vehicle is parked")
            return True

        print("Vehicle is not parked")
        return False


class Bike(Vehicle):
    pass


class Scooter(Vehicle):
    pass


class Car(Vehicle):
    pass


class Bus(Vehicle):
    pass


class ParkZone:
    def __init__(self):
        self.space_available = 10
        self.parked = {}
        
    def generate_token(self):
        return randrange(1111, 9999)

    # Time: O(n) Space: O(1)
    def park(self, vehicle):
        if self.is_space_available(vehicle.size):
            token = self.register(vehicle)
            self.space_available -= vehicle.size
            vehicle.parked = True
            print(vehicle.model, " has been parked.")
            print("Token: ", token, ", Space available ", self.space_available)
            return token
        print("No space available")
        return None

    # Time: O(1) Space: O(1)
    def is_space_available(self, size):
        return (self.space_available - size) >= 0

    # Time: O(n) Space: O(1)
    def register(self, vehicle):
        token = self.generate_token()
        while token in self.parked:
            token = self.generate_token()
        self.parked[token] = vehicle
        return token

    # Time: O(1) Space: O(1)
    def depark(self, token):
        if token in self.parked:
            parked_vehicle = self.parked[token]
            parked_vehicle.parked = False
            self.space_available += parked_vehicle.size
            print(parked_vehicle.model, "has been deparked")
            print("Space Available: ", self.space_available)
            return self.parked.pop(token)
        raise ValueError("Invalid token or vehicle not found")

    # Time: O(n) Space: O(1)
    def list_parked_vehicles(self):
        print("------Parked Vehicles------")
        for vehicle in self.parked.values():
            print(vehicle.model, vehicle.size, vehicle.number)
