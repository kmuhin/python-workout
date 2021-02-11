#!/usr/bin/env python3

class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
    
    def brake(self):
        """
        Stop the car
        """
        return "Braking"
    
    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"

if __name__ == "__main__":
    car = Vehicle("blue", 5, 4)
    print(f"car's color is {car.color}")
    
    truck = Vehicle("red", 3, 6)
    print("truck's color is ",truck.color)


sample=Vehicle("yellow",1,1)
print(sample.brake())
print(sample.color)