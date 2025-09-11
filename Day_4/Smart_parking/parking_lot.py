from parking_spot import ParkingSpot

class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            print(
                f"Spot ID: {spot.get_id()} | Size: {spot.get_size()} | Status: {spot.get_status()} | Vehicle: {spot.get_vehicle()}"
            )

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.get_status() == "Free":
                if spot.assign_vehicle(vehicle):
                    return
        print("No suitable spot available!")

    def unpark_vehicle(self, vehicle, hours, payment_method):
        for spot in self.spots:
            if spot.get_status() != "Free" and spot.get_vehicle() == vehicle:
                fee = spot.remove_vehicle(hours)
                payment_method.pay(fee)
                return
        print("Vehicle not found in parking lot!")
