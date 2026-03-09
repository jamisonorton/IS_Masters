# 1.1. Hello World (again) (3 points)
# Write a function that asks for the user’s name and prints “Hello, “ followed by their name.
def hello_world(name):
    return f"Hello, {name}"


full_name = input("What is your full name? ")
print(hello_world(full_name))


# 1.2. Dog Years (3 points)
# Write a function that asks for the age of the user’s dog.
# Print a string that states the dog’s age in dog years with a conversion rate of 1 human year to 7 dog years.


def years_to_dog_years(age):
    return age * 7


dog_age = int(input("How old is your dog? "))
print(f"Your dog is {years_to_dog_years(dog_age)} years old in dog years.")


# 1.3. Purchase (3 points)
# Write a function that asks for the user to enter a number of items they wish to purchase.
def purchages(num_items):
    return f"You wish to purchase {num_items} items"


user_purchases = int(input("How many items do you wish to purchase? "))
print(purchages(user_purchases))
