# 1. Name function (5 points)
# Write a function that takes 3 strings - first name, last name and middle initial.
# Return one string that has the person’s full name.  Make sure that the first letter of each name is capitalized (.title()) and then return the string.
# Use the .format() string function in the return statement.
def full_name(first_name, last_name, middle_initial):
    first_name = first_name.title()
    last_name = last_name.title()
    middle_initial = middle_initial.title()

    return str.format(first_name + " " + middle_initial + " " + last_name)


first_name = input("What is your First name? ")
last_name = input("What is your Last name? ")
middle_initial = input("What is your Middle initial? ")

print("Your name is:", full_name(first_name, last_name, middle_initial))


# 2. String function practice (5 points)
# 1.) Using escape characters, print out the phrase “Welcome to O’Neil’s Boat Rentals!”
# 2.) Initialize one string variable to the following sentence:
# “Hello there! How are you? I'm doing fine."

# Using the print() function and escape characters, make the output look exactly as below: (Be sure there’s a single quote in the word I’m.

# Code Example:
# Hello there!
# How are you?
# I'm doing fine.
# 3.) Initialize a string variable to “hello python” and print it out in all uppercase using a string function.
# 4.) Write a small program using a ‘while’ loop (while True).
# 1.) Prompt the user to enter their age.
# 2.) Using a string function, check if the input is a decimal value, if true then break from the loop.
# 3.) Continue prompting the user until a whole number (isdecimal) has been entered.
# 5.) Using a string function, print your first and last name with the * symbol on both sides of your name with a max of 25 characters.
