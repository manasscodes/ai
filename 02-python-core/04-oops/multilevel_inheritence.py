# Multilevel Inheritance
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class SportsCar(Car):
    def feature(self):
        print("This is a sports car")

sc = SportsCar()
sc.info()
sc.wheels()
sc.feature()