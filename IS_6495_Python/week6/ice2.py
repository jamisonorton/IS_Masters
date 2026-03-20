# 1. Divide by zero exception (5 points)


# Create a function that will divide 2 numbers and return the result. The function will accept 2 arguments. Use a try statement and the ZeroDivisionError exception type to catch divide by zero errors. Inside the exception, print out “invalid argument”.
def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("invalid argument")


division(9, 0)

# 2. Basic exception handling (5 points)

# Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ["a", "b", "c"]:
        print(i**2)
except TypeError as ex:
    print(ex)


# 3. try-except-finally (5 points)

# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError as ex:
    print(ex)
finally:
    print("All Done.")

# 4. try-except-else(5 points)

# Write a function that asks for an integer and prints the square on it. Use a while loop with try, except, else block to account for incorrect inputs.


def squared():
    while True:
        try:
            user_integer = int(input("Please input an integer: "))
        except ValueError:
            print("An error occurred! Please try again!")
        else:
            print(f"Thank you, your number squared is: {user_integer ** 2}")
            break


squared()

# Output example:

# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, your number squared is: 4
