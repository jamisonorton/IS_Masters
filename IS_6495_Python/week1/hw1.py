###### Part 1 ########
# Exercise 1: Understanding Variables (2 points)

# a. Explain in your own words what a variable is in Python and how it applies in programming.

# b. Write a Python program that:
#    - Declares a variable `greeting_message` and assigns it the value `"Hello, Python Learner!"`
#    - Prints the value of `greeting_message`
#    - Changes the value of `greeting_message` to `"Keep coding and learning!"` and prints it again.

# a.) A variable in python is a named location used to store data in memory. It is assigned using the assignment operator =.

# b.)

greeting_message = "Hello, Python Learner!"
print(greeting_message)
greeting_message = "Keep coding and learning!"
print(greeting_message)

###### Part 2 ########

full_name = "Jamison Orton"
print(f"Name in title case:", full_name.title())
print(f"Name in uppercase:", full_name.upper())
print(f"Name in lowercase:", full_name.lower())
print(f"Hello, {full_name}! Welcome to Python programming.")

###### Part 3 ########
# python
# message = "Python is fun!"
# print(mesage)
# a. What kind of error does this code produce?
# b. Why does this error occur?
# c. Provide the corrected version of the code.

# a and b.) The first error that is produced is a NameError because python is not defined.
# Traceback (most recent call last):
#   File "/Users/jorton4/Documents/personal-repos/IS_Masters/IS_6495_Python/Week 1/hw1.py", line 27, in <module>
#     python
# NameError: name 'python' is not defined

# a and b.) Once you comment out python and you are left with just the message you get a mesage not defined because you misspelled the variable message that you defined earlier.

# c.)
python = "This is dumby code cause you don't really use it."
message = "Python is fun!"
print(message)

###### Part 4 ########
# Write a Python program that performs the following mathematical operations and prints the results:
# - Adds two numbers to get 10
# - Subtract two numbers to get 5
# - Multiplies two numbers to get 24
# - Divide two numbers to get 3.5
# - Uses the exponent operator (`**`) to calculate 2 to the power of 5

add_nums = 2 + 8
print(add_nums)
subtract_nums = 7 - 2
print(subtract_nums)
multiply_nums = 6 * 4
print(multiply_nums)
divide_nums = 21 / 6
print(divide_nums)
exponent_nums = 2**5
print(exponent_nums)

###### Part 5 ########
# Exercise 5: Pay Calculation with Hours and Minutes (2 points)
# Create two variables to hold values for hourly wage and minutes worked for a project.
# Assign hourly_wage = 22 and minutes_worked = 390.
# Calculate the total hours worked (note that 1 hour = 60 minutes) and then calculate the total pay.
# Using the print function, display the pay results with a dollar sign before the value. (For example, $126)

hourly_wage = 22
minutes_worked = 390

total_hours_worked = minutes_worked / 60
total_pay = total_hours_worked * hourly_wage
print(f"${int(total_pay)}")
