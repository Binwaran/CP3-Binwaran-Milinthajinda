class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirCoditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirCoditioner()

picUp1 = PickUp()
picUp1.turnOnAirCoditioner()

van1 = Van()
van1.turnOnAirCoditioner()

estatecar1 = Estatecar()
estatecar1.turnOnAirCoditioner()


