import numpy as np
from datetime import time

class Supermarket:
    def __init__(self):
        location_names = ['entry', 'dairy', 'drinks', 'fruit', 'spices', 'checkout']
        self.locations = {location_name: Location(location_name) for location_name in location_names}

    def open(self):
        self.time = time(7)

    def close(self):
        ## send customers to checkout
        return True

    def get_entry_location(self):
        return self.locations['entry']

class Customer:
    def __init__(self, id, entry_time, entry_location):
        self.id = id
        self.location = entry_location
        self.history = [Timestamp(entry_time, self.location)]

    def get_last_timestamp(self):
        return self.history[len(self.history) - 1]

class Location:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def __str__(self):
        return f'Location: {self.name}'

class Timestamp:
    def __init__(self, time, location):
        self.time = time
        self.location = location

if __name__ == '__main__':
    supermarket = Supermarket()
    [print(location) for location in supermarket.locations]
    supermarket.open()
    print(f'{supermarket.time}')

    customer = Customer(1, supermarket.time, supermarket.get_entry_location())
    print(f'Customer is at {customer.location} at time {customer.get_last_timestamp().time}')

    # for loop that checks if the supermarket is before 21:50
    #   If so then incerement one minute and simulate generation/movement of customers
    #   Else close store and send current customers to checkout