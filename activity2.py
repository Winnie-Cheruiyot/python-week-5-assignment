# Base class for vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("The move() method must be defined in subclasses")

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Subclass representing a Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Create objects of each class
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Calling the move() method on each object
vehicles = [car, plane, boat, bicycle]

for vehicle in vehicles:
    vehicle.move()  # Demonstrating polymorphism where each class defines move differently
    # Each subclass has its own implementation of the move method, demonstrating polymorphism
