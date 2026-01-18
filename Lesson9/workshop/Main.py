from Lesson9.workshop.Vehicles.Car import Car
from Lesson9.workshop.Vehicles.ElectricCar import ElectricCar
from Lesson9.workshop.Vehicles.Motorcycle import Motorcycle


from Lesson9.workshop.Engine.CombustionEngine import CombustionEngine
from Lesson9.workshop.Engine.ElectricEngine import ElectricEngine

combustion_engine = CombustionEngine(150, "petrol")
electric_engine = ElectricEngine(140, 75)

car = Car("Polonez", 1400, combustion_engine, 5)
motorcycle = Motorcycle("Yamaha", 220, combustion_engine)
electric_car = ElectricCar("Tesla", 1900, electric_engine, 5)

vehicles = [car, motorcycle, electric_car]

for vehicle in vehicles:
    vehicle.drive()
    vehicle.stop()
    print("**************************")