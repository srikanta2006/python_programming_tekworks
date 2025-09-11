class ParkingSpot:
    def __init__(self, spot_id, size):
        self.__spot_id = spot_id
        self.__size = size  
        self.__is_free = True
        self.__vehicle = None

    # --- Getter methods for encapsulation ---
    def get_id(self):
        return self.__spot_id

    def get_size(self):
        return self.__size

    def get_vehicle(self):
        return self.__vehicle

    def get_status(self):
        return "Free" if self.__is_free else f"Occupied by {self.__vehicle.get_license_plate()}"

    # --- Business logic ---
    def assign_vehicle(self, vehicle):
        if not self.__is_free:
            print(f"Spot {self.__spot_id} already occupied!")
            return False

        if self.__is_vehicle_fit(vehicle):
            self.__vehicle = vehicle
            self.__is_free = False
            print(f"Vehicle {vehicle.get_license_plate()} parked at Spot {self.__spot_id}")
            return True
        else:
            print(f"Vehicle {vehicle.get_license_plate()} does not fit Spot {self.__spot_id} ({self.__size})")
            return False

    def remove_vehicle(self, hours):
        if self.__is_free:
            print(f"Spot {self.__spot_id} is already empty!")
            return 0

        fee = self.__vehicle.calculate_parking_fee(hours)
        print(f"Vehicle {self.__vehicle.get_license_plate()} unparked from Spot {self.__spot_id}, Fee: ₹{fee}")
        self.__vehicle = None
        self.__is_free = True
        return fee

    # --- Private helper method ---
    def __is_vehicle_fit(self, vehicle):
        size_rules = {
            "Bike": ["S", "M", "L", "XL"],
            "Car": ["M", "L", "XL"],
            "SUV": ["L", "XL"],
            "Truck": ["XL"]
        }
        return self.__size in size_rules[vehicle.__class__.__name__]
