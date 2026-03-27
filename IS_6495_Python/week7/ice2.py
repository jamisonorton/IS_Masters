# Exercise 2 – Class Introduction

#  There are 3 problems, each worth 5 points with a total of 15 points. Submit your .py file to canvas.


# #2.1. The simplest class: (5 points)


# We will start with the simplest class you could ever write in Python. Create a class called Simplest() and use the pass statement.


class Simplest:
    pass


# Answer the following questions:

# a. Using the code below, what type is this object?

print(type(Simplest))
# It is the <class 'type'>.

# b. Create an instance of Simplest to a variable called simp. What type is simp?
simp = Simplest()
print(type(simp))
# simp is a <class '__main__.Simplest'> so it is of type Simplest.

# #2.2. Person Class: (5 points)

# Create a new class called Person. Add 3 attributes (or fields) called first_name, middle and last_name.


class Person:
    first_name = ""
    middle = ""
    last_name = ""

    def format_name(self):
        first_name = self.first_name.title()
        middle = self.middle.title()
        last_name = self.last_name.title()

        return "{} {}. {}".format(first_name, middle, last_name)


# Add a function called format_name() and return all 3 attributes.

# (Hint: Use the same function we wrote in week 6).

# Create a new instance of the Person class, set the attribute fields and then call the format_name() function using print().
person_a = Person()
person_a.first_name = "Jamison"
person_a.middle = "A"
person_a.last_name = "Orton"

full_name = person_a.format_name()
print(full_name)

# #2.3. Cylinder: (5 points)

# Create a Cylinder class using the class skeleton below. Fill in the code needed for each function.
import math


class Cylinder:

    def set_height_radius(self, height, radius):

        self.height = height
        self.radius = radius

    def volume(self):

        vol = self.height * math.pi * (self.radius**2)

        return round(vol, 2)

    def surface_area(self):

        top = math.pi * self.radius**2
        area = 2 * top + (2 * math.pi * self.radius * self.height)

        return round(area, 2)


# Sample output should look like this:

mycyl = Cylinder()
mycyl.set_height_radius(2, 3)
print(mycyl.volume())
# 56.52
print(mycyl.surface_area())
# 94.2

# Volume formula:

# height * pi(radius)^2

# Surface area formula: top = pi * radius^2

# 2*top + (2*pi*radius*height)
