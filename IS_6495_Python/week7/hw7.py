# Exercise #1: (5 points)

# Here is a Person class definition:
# import datetime
# class Person:
#     def __init__(self, name, surname, birthdate, address, telephone, email):
#         self.name = name
#         self.surname = surname
#         self.birthdate = birthdate
#         self.address = address
#         self.telephone = telephone
#         self.email = email
#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1
#         return age
# person = Person(
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12),  # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jane.doe@example.com",
# )
# print(person.name)
# print(person.email)
# print(person.age())

# Explain what the following variables refer to, and their scope:

### Person is the class that you created globally scoped
### person is an instance of the class that is globally scoped
### surname is a parameter in __init__ that is locally scoped to __init__
### self refers to the current instance that is locally scoped to the class
### age (the function name) method of the class that is class scoped
### age (the variable used inside the function) local variable that exists only inside the age() method
### self.email instance variable belonging to the person object. Locally scoped through the instance
### person.email accessing the instance variable through the global object person


# Exercise #2: (5 points)

# Rewrite the Person class so that a person’s age is calculated for the first time when a new person instance is created, and recalculated (when it is requested)
# if the day has changed since the last time that it was calculated.

import datetime


class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

        self._age = None
        self._age_last_recalculated = None
        self.recalculate_age()

    def age(self):

        if datetime.date.today() > self._age_last_recalculated:
            self.recalculate_age()

        return self._age

    def recalculate_age(self):
        today = datetime.date.today()

        # todo: set local variable "age", subtract today's year from birthdate year. age = ...
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        # todo: set the age class variable to the new age value calculated from above.
        self._age = age
        # todo: set a new class variable _age_last_recalculated to equal today.
        self._age_last_recalculated = today


person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12),  # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com",
)

# Invoke the new recalculate_age() function in both the constructor and age() function.
print(person.age())

# Exercise #3: (5 points)

# Create a new class called Square. Implement a constructor that takes a "side" parameter and initialize it to a class member called "side".
# Add a function in the class called area(). The area() function will return the side^2. Create an instance of the class and invoke the area() function to test it.
# Set the instance variable "side" to a different value and invoke area() again.


class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


square = Square(2)
print(square.area())

square.side = 5
print(square.area())


# Exercise #4: (5 points)

# Create an instance of the Person class from exercise 1. Use the dir function on the instance. Then use the dir function on the class.
person_4 = Person(
    "John",
    "Doe",
    datetime.date(1994, 8, 12),  # year, month, day
    "3459 E 1180 S, Spanish Fork, UT 84660",
    "123 456 7891",
    "john.doe@example.com",
)

print(dir(person_4))
print(dir(Person))


# What happens if you call the __str__ method on the instance? Verify that you get the same result if you call the str function with the instance as a parameter.
### If you call the __str__ method on the instance it returns a string representation of the object.
# What is the type of the instance?
### <class '__main__.Person'>
# What is the type of the class?
### <class 'type'>
# Write a function which prints out the names and values of all the custom attributes of any object that is passed in as a parameter. (see vars() hint.)
def print_vars(val):
    print(vars(val))


print_vars(person_4)


# Exercise #5: (5 points)


# Write a Python class to reverse a string word by word.
class ReverseString:

    def __init__(self, string1):
        self.string1 = string1

    def reverse(self):
        split_string = self.string1.split()
        split_list = split_string[::-1]
        return " ".join(split_list)


string_1 = ReverseString("This is a string")

print(string_1.reverse())

# Exercise #6: (5 points)

# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
# Area Formula: radius squared * pi (r2 * 3.14)
# Perimeter Formula: 2*radius*pi
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return self.radius**2 * math.pi

    def compute_perimeter(self):
        return 2 * math.pi * self.radius


circle_1 = Circle(5)
print(circle_1.compute_area())
print(circle_1.compute_perimeter())

# Exercise #7: (5 points)

# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
# Formula: Length * Width


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width


rectangle_1 = Rectangle(2, 4)
print(rectangle_1.compute_area())


# Exercise #8: (5 points)

# Create a Line class using the class skeleton below. Fill in the code needed for each function.

# (Hint: coor1, coor2 are tuples)
import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


# Sample output:

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
# 9.433981132056603

print(li.slope())
# 1.6

# Slope Formula:
# m = (y2 - y1) / (x2 - x1)

# Distance Formula:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)


# Exercise #9: (5 points)

# Step 1:
# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

# Step 2:
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.
# Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why.
# Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”
# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.


# Solution: (Freebee)


def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


n = input("Give me a number: ")

while n != 1:
    n = collatz(int(n))
