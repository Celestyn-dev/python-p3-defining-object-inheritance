import sys
import os

# Add the lib folder to the Python path so we can import vehicle and car
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from vehicle import Vehicle
from car import Car

# Test the Vehicle class
vehicle = Vehicle("medium", 4)
print("Vehicle go:", vehicle.go())
print("Vehicle fill up:", vehicle.fill_up_tank())
print("Vehicle wheel size:", vehicle.wheel_size)
print("Vehicle wheel number:", vehicle.wheel_number)

print()

# Test the Car class
car = Car("large", 4)
print("Car go:", car.go())  # Overridden method
print("Car fill up:", car.fill_up_tank())  # Inherited method
print("Car wheel size:", car.wheel_size)
print("Car wheel number:", car.wheel_number)

print()

# Introspection
print("Car.__bases__:", Car.__bases__)
print("Vehicle.__bases__:", Vehicle.__bases__)
print("int.__bases__:", int.__bases__)
print("Car.__class__:", Car.__class__)
print("int.__class__:", int.__class__)
