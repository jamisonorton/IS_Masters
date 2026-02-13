###### Part 1 ########
# 1. Understanding Data Types
# Given the following Python expressions, determine the data type of the result:
type(3 + 4)  # This is type int. It is a number without a decimal.
type(3.0 + 4)  # This is a float as it has a decimal
type(5 / 2)  # This is a float as it results in a decimal
type(5 // 2)  # This is a int as it does not have a decimal
type("Python")  # This is a string as it is a word.
# Write your answers and explain why each data type is assigned.


###### Part 2 ########
# 2. Variable Naming Rules
# Which of the following variable names are valid in Python? If invalid, explain why.
# 1message = "Hello" <- This is invalid as it starts with a number.
# _message = "Python" <- This is valid.
# message_1 = "Coding" <- This is valid.
# print = "Variable" <- This is invalid because it uses the name of a built in function
# student name = "John" <- This is invalid because it has a space.

###### Part 3 ########
# The following program contains an error. Fix the mistake so that it runs correctly.

message = "Welcome to Python Programming"
print(message)

###### Part 4 ########
# 4. Performing Basic Math Operations
# Write a Python program that calculates and prints:
# •    The sum of 8 and 12.
# •    The difference between 50 and 23.
# •    The product of 6 and 7.
# •    The result of 36 divided by 6.
# •    The result of 2 raised to the power of 4.

print(8 + 12)
print(50 - 23)
print(6 * 7)
print(36 / 6)
print(2**4)

###### Part 5 ########
# 5. Understanding Order of Operations
# Predict the output of the following expressions before running them in Python:
# print(5 + 3 * 2) <- 11
# print((5 + 3) * 2) <- 16
# print(10 - 3 ** 2) <- 1
# print(16 / 4 + 2) <- 6.0
# Then, run the code and compare the results with your predictions.
print(5 + 3 * 2)
print((5 + 3) * 2)
print(10 - 3**2)
print(16 / 4 + 2)

# My predictions were exactly correct with the output.
