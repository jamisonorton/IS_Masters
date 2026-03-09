# 1.1. Hello World (again) (3 points)
# Write a function that asks for the user’s name and prints “Hello, “ followed by their name.
def hello_world(name):
    return name


full_name = input("What is your full name? ")

print("Hello,", hello_world(full_name))


# 1.2. Dog Years (3 points)
# Write a function that asks for the age of the user’s dog.
# Print a string that states the dog’s age in dog years with a conversion rate of 1 human year to 7 dog years.


def years_to_dog_years(age):
    return age * 7


dog_age = input("How old is your dog? ")

print("Your dog is", years_to_dog_years(int(dog_age)), "years old.")


# 1.3. Purchase (3 points)
# Write a function that asks for the user to enter a number of items they wish to purchase.
def purchages(num1):
    return num1


user_purchases = input("How many items do you wish to purchase? ")

print("You are purchasing", purchages(int(user_purchases)), "items")
