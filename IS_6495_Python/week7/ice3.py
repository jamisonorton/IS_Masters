# Exercise 3 – Class & Constructors

#  There are 3 problems, each worth 5 points with a total of 15 points. Submit your .py file to canvas.


# #3.1. NumberSet Class (5 points)


# Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers.
# Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.
class NumberSet:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


t = NumberSet(6, 10)

# #3.2. Animal Class (5 points)

# Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs.
# Create an instance method called limbs that, when called,
# returns the total number of limbs the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs.
# Call the limbs method on the spider instance and save the result to the variable name spidlimbs.

# Here's an empty skeleton class:


class Animal:

    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def get_arms(self):
        return self.arms

    def get_legs(self):
        return self.legs

    def limbs(self):
        return self.arms + self.legs


spider = Animal(4, 4)
spidlimbs = spider.limbs()


# #3.3. Cereal Class (5 points)

# Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor:
# name, brand, and fiber. When an instance of Cereal is printed, the user should see the following:
# “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!”


class Cereal:

    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"


c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)
print(c1)
print(c2)

# To the variable name c1, assign an instance of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2.

# To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3.

# Practice printing both!

# class Cereal:
#     pass
# """class called Cereal that accepts three inputs in the Ctor: 2 strings and 1
# integer, and assigns them to 3 instance variables in the constructor:
# name, brand, and fiber."""
