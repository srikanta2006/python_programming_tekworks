from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate
        self.__owner_name = owner_name


    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, license_plate):
        self.__license_plate=license_plate

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, owner_name):
        self.__owner_name=owner_name

    def display(self):
        print(f"Onwer name: {self.__owner_name}")
        print(f"Number plate: {self.__license_plate}")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        super().display()
        print(f"Helmet required: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return hours*20


class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        super().display()
        print(f"Number of seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return hours*50


class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        super().display()
        print(f"Four wheel drive: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return hours*70


class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity=10000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        super().display()
        print(f"max load capacity: {self.max_load_capacity}")

    def calculate_parking_fee(self, hours):
        return hours*100