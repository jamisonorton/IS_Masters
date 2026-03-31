# Exercise 1 – Class Inheritance


# #1.1. Ice Cream Shop inherits from Restaurant (5 points)

# Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote.
# Add an attribute of flavors to the __init__() for IceCreamStand. Make a method called get_flavors() that will display the flavors for this ice cream shop.
# Create an instances of the ice cream class and call the get_flavors() method.


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + "\n" + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open for business")


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.ice_cream_flavors = flavors

    def get_flavors(self):
        print(self.ice_cream_flavors)


# Usage Example:
restaurant = Restaurant("My Fancy Restaurant", "Fine Dining")
restaurant.describe_restaurant()
restaurant.open_restaurant()

ice_cream = IceCreamStand(
    "My Ice Cream Shoppe", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"]
)
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.get_flavors()


# #1.2. Admin inherits from User (5 points)

# Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

# Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote.
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.


class User:
    _first_name = ""
    _last_name = ""
    _username = ""
    _email = ""
    _DOB = ""
    _address = ""
    _phone_number = ""

    def __init__(
        self, first_name, last_name, username, email, DOB, address, phone_number
    ):
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._email = email
        self._DOB = DOB
        self._address = address
        self._phone_number = phone_number

    def describe_user(self):
        print(
            self._first_name,
            self._last_name,
            self._username,
            self._email,
            self._DOB,
            self._address,
            self._phone_number,
            sep="\n",
        )

    def greet_user(self):
        print(
            "Hello " + self._first_name + " " + self._last_name + " nice to meet you!"
        )


class Admin(User):

    def __init__(
        self,
        first_name,
        last_name,
        username,
        email,
        DOB,
        address,
        phone_number,
        privileges,
    ):
        super().__init__(
            first_name, last_name, username, email, DOB, address, phone_number
        )
        self._privileges = privileges

    def show_privileges(self):
        print(self._privileges)


# Regular users
user1 = User(
    "Emily",
    "Carter",
    "ecarter1",
    "emily@test.com",
    "May 10, 1998",
    "45 Oak Street",
    "8011112222",
)

user2 = User(
    "Michael",
    "Reed",
    "mreed2",
    "michael@test.com",
    "January 4, 1995",
    "78 Pine Avenue",
    "8013334444",
)

user3 = User(
    "Sophie",
    "Allen",
    "sallen3",
    "sophie@test.com",
    "March 22, 2001",
    "12 Maple Drive",
    "8015556666",
)

# Admin users
admin1 = Admin(
    "Jamison",
    "Orton",
    "jorton4",
    "jamison@test.com",
    "August 8, 2020",
    "123 Main Street",
    "8014228282",
    ["can add post", "can delete post", "can ban user"],
)

admin2 = Admin(
    "Rachel",
    "Brown",
    "rbrown5",
    "rachel@test.com",
    "July 15, 1992",
    "99 Center Street",
    "8017778888",
    ["can reset passwords", "can suspend accounts", "can manage users"],
)

admin3 = Admin(
    "David",
    "Lee",
    "dlee6",
    "david@test.com",
    "November 2, 1989",
    "250 Hill Road",
    "8019990000",
    ["can edit settings", "can approve posts", "can remove comments"],
)

# Call methods for regular users
user1.greet_user()
user1.describe_user()
print()

user2.greet_user()
user2.describe_user()
print()

user3.greet_user()
user3.describe_user()
print()

# Call methods for admins
admin1.greet_user()
admin1.describe_user()
admin1.show_privileges()
print()

admin2.greet_user()
admin2.describe_user()
admin2.show_privileges()
print()

admin3.greet_user()
admin3.describe_user()
admin3.show_privileges()
