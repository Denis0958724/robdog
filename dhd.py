#
#
# class Student:
#     amount_of_students = 0
#     def __init__(self, name, age, height = 160):
#         self.age = age
#         self.height = height
#         self.name = name
#         Student.amount_of_students += 1
#
#     def happy_birthday(self):
#         print(f'Greetings! {self.name} you have HB!')
#         self.age += 1
#
#     def __str__(self):
#         return f'<Student name={self.name} age={self.age} height={self.height}>'
#
#
# s1 = Student('Alex', 28, 180)
# s1.happy_birthday()
# print(s1)
#
# s2 = Student('Bob', 18, 170)
# print(s2)
#
# s3 = Student('Jane', 17, 150)
# print(s3)
#
# print('Amount', Student.amount_of_students)
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calc_area(self):
#         return 3.14 * self.radius ** 2
# circle_10 = Circle(10)
# print(circle_10.calc_area())
#
# circle_3 = Circle(3)
# print(circle_3.calc_area())


import random
from tkinter.font import names


class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.skills = 0
        self.alive = True

    def to_walk(self):
        print('time to walk')
        self.skills += 0.07
        self.gladness += 5

    def to_brewed(self):
        print('brewed')
        self.skills -= 0.01
        self.gladness -= 8


    def to_sleep(self):
        print('time to sleep')
        self.gladness += 4
        self.skills -= 0.2


    def to_eat(self):
        print('time to eat')
        self.gladness += 6
        self.skills += 0.02

    def is_alive(self):
        if self.skills < -10:
            print('Uncontrollable')
            self.alive = False
        elif self.gladness <= 0:
            print('Nobody needs it')
        elif self.skills > 10:
            print('Our dog knows how to make commands!')
            self.alive = False




    def end_of_day(self):
        print(
            f"gladness - {self.gladness}\n"
            f"skills - {round(self.skills,2)}"
        )

    def live(self, day):
        print(
            f'Day #{day} of {self.name}'
        )
        magic = random.randint(1, 3)
        if magic == 1:
            self.to_walk()
        elif magic == 2:
            self.to_eat()
        elif magic == 3:
            self.to_sleep()
        elif magic == 4:
            self.to_brewed()

        self.end_of_day()
        self.is_alive()


Robbi = Dog('Robbi')
for day in range(365):
    if Robbi.alive == False:
        break
    Robbi.live(day)


