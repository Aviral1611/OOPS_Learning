class Car:

    def __init__(self,make,model,year,colour,for_sale):
        self.make = make
        self.model = model
        self.year = year 
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.colour}{self.model}")

    def stop(self):
        print(f"This {self.colour}{self.model} is stopped")

    def describe(self):
        print(f"This car is a {self.year} {self.colour} {self.model}")


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1 
