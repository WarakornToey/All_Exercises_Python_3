class Vehicle: # Class หลัก
     licenseCode = ""
     serialCode = ""
     face_ID = ""
     def turnOnAir(self):
        print("Turn On Air")

class Car(Vehicle): # class สืบทอด จาก class Vehicel
    print("Car Turn On Air")
    
class Pickup(Vehicle): # class สืบทอด จาก class Vehicel
    print("Pickup Turn On Air")

class Van(Vehicle): # class สืบทอด จาก class Vehicel
    print("Van Turn On Air")

class Estatecar(Vehicle): # class สืบทอด จาก class Vehicel
    print("Estatecar Turn On Air")

Car1 = Car()
Pickup1 = Vehicle()
Van1 = Van()
Estatecar1 = Estatecar()
