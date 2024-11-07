from app import Car
from app import Student

car1 = Car('nice','Mustang','2024','Black',False)
car2 = Car('Bad','Ford','2023','Red',True)
car3 = Car('Good','Tesla','2022','White',True)
car4 = Car('Average','Toyota','2021','Blue',False)
car5 = Car('Excellent','BMW','2020','Grey',True)

student1 = Student("Mike",20)
student2 = Student("Charan",28)

print(car1.model)
print(car2.model)
print(car3.model)
print(car4.model)
print(car5.model)

car1.drive()
car2.stop()
car4.describe()

print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_students)
