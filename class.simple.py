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
    print("truck's color is ", truck.color)

sample = Vehicle("yellow", 1, 1)
print(sample.brake())
print(sample.color)


class Foo:
    bar = []

    def __init__(self, x):
        self.bar.append(x)


class Foo2:
    def __init__(self, x):
        self.bar = []
        self.bar.append(x)


f1 = Foo(42)
g1 = Foo(55)
f2 = Foo2(42)
g2 = Foo2(53)

print(f1.bar)
print(g1.bar)
print(f2.bar)
print(g2.bar)


class A:
    class_var = 'Test'
    class_list = []

    def __init__(self):
        pass

    def set_class_1(self, text):
        # sets class variable
        A.class_var = text
        A.class_list.append(text)

    def set_class_2(self, text):
        # sets class variable
        # the same as above and more convinient for renaming class
        Type(self).class_var = text
        Type(self).class_list.append(text)

    def set_instance(self, text):
        # sets instance variable
        self.class_var = text
        self.class_list.append(text)


a = A()
b = A()


def print_ab():
    print(f'a: {a.class_var} b: {b.class_var}')
    print(f'a: {a.class_list}')
    print(f'b: {b.class_list}')


a.set_class_1(1)
print_ab()
a.set_class_1(2)
print_ab()
a.set_instance(3)
# str is immutable var. a made a copy class_var
# list is mutable var. a and b still refer to the same list
print_ab()
