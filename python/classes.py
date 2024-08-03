#A class in Python is a blueprint for creating objects. It encapsulates data for the object and methods to manipulate that data.

# Instance vs Class Members
# Instance members are attributes and methods that belong to a specific instance of a class.
# Class members are attributes and methods that belong to the class itself rather than any specific instance.

class Car:
    wheels = 4  # Class member

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"

obj = Car("swift", "xz")
print(obj.display_info())
print(Car.wheels)

#magic fucntions
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

    def __repr__(self):
        return f"'{self.make}', model='{self.model}'"
      
print(Car("swift","xz"))
print(repr(Car('Toyota', 'Corolla')))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __str__(self):
        return f"{self.x} , {self.y}"

a = Point(10,20)
b = Point(20,10)
print(a + b)


#properties
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age  # Internal attribute to be managed with a property
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


person = Person('Alice', 30)
print(person.age)


#inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.num_doors = num_doors

    def honk(self):
        return "Beep beep!"

my_car = Car('Toyota', 'Corolla', 4)

#without super
class Vehicle:
    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        self.make = make
        self.model = model  # Call the constructor of the parent class
        self.num_doors = num_doors

    def honk(self):
        return "Beep beep!"

my_car = Car('Toyota', 'Corolla', 4)
print(my_car.make)


#method over riding
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start_engine(self):
        return "Vehicle engine started"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def start_engine(self):
        return "Car engine started"

# Create a Car object
my_car = Car('Toyota', 'Corolla', 4)

# Call the overridden method
print(my_car.start_engine())  # Output: Car engine started



#abstract classes
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


#Polymorphism is a concept that allows objects of different classes to be treated as objects of a common superclass.
# Allows different classes to have methods with the same name but different implementations. This is a form of polymorphism where a subclass method overrides a parent class method.

