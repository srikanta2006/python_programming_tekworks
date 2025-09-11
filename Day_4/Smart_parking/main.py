from vehicles import Bike, Car, SUV, Truck
from parking_lot import ParkingLot
from parking_spot import ParkingSpot
from payments import CashPayment, CardPayment, UPIPayment
if __name__ == "__main__":

    v1 = Bike("AP09XY1234", "Srikanta")
    v2 = Car("TS07AB5678", "Vrushank")
    v3 = SUV("KA01CD9999", "Ravi")
    v4 = Truck("MH20EF4321", "Arjun")


    vehicles = [v1, v2, v3, v4]
    for v in vehicles:
        v.display()

    print("\n--- Parking Lot Setup ---")
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))

    lot.show_spots()

    print("\n--- Parking Vehicles ---")
    lot.park_vehicle(v1)
    lot.park_vehicle(v2)
    lot.park_vehicle(v3)
    lot.park_vehicle(v4)
    lot.show_spots()

    print("\n--- Unparking Vehicles ---")
    lot.unpark_vehicle(v1, 2, UPIPayment())  
    lot.unpark_vehicle(v2, 3, CardPayment())
    lot.unpark_vehicle(v3, 1, CashPayment())  
    lot.unpark_vehicle(v4, 5, UPIPayment())   