###### Part 1 ########
# 1. Simple Message
# Write a Python program that:
# •    Assigns a message to a variable called message
# •    Prints the message
# •    Changes the value of message to a new text and prints it again.

message = "This is a simple message"

print(message)

message = "this is an updated simple message"

print(message)

###### Part 2 ########
# 2. Variable Naming Rules
# Which of the following variable names are valid in Python? If a name is invalid, explain why.
#  1st_message = "Hello" <- This is not a valid name because it starts with a number
#  greeting message = "Hi" <- This is not a valid name because it contains a space
#  _message = "Secret" <- This is a valid name
#  name@user = "John" <- This is not a valid name because it cannot contain special characters
#  favoriteNumber = 7 <- This is a valid name (however it does not follow PEP 8 style guides)

###### Part 3 ########
# The following code contains an error.
# a. Identify the error and explain why it occurs.
# b. Correct the error so the program runs successfully.

# greeting = "Welcome to Python Programming!"
# print(Greeting) <- The error is occuring because you are calling a variable Greeting which does not exist as the variable assigned was greeting.

greeting = "Welcome to Python Programming!"
print(greeting)

###### Part 4 ########
# 4. String Case Methods
# Write a Python program that:
# •    Assigns your name to a variable my_name
# •    Prints your name in title case, uppercase, and lowercase using string methods.

my_name = "Jamison Orton"
print(my_name.title())
print(my_name.upper())
print(my_name.lower())

###### Part 5 ########
# 5. Mathematical Operations
# Write a Python program that:
# Stores two numbers in variables a and b
# Performs and prints the results of:
# Addition
# Subtraction
# Multiplication
# Division
# Exponentiation (a**b)
# Please submit answers in a document.

a = 2
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a**b)
