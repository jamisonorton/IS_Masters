# 2.1. Sum of numbers (3 points)
# Write a function that takes a list of numbers and returns the sum of the numbers.
crappy_list = [1, 15, 25, 50, 100]


def sum_from_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_from_list(crappy_list))


# 2.2. Number power (3 points)
# Write a function that takes two integers and raises the first number to the power of the second number and returns the result.


def num_power(num1, num2):
    return num1**num2


print(num_power(3, 4))

# 2.3. Tax function (3 points)
# Write a function that takes the price of the item as an argument and return the price calculated with a tax value of .07.
# The goal here is to convert the tax calculation into a reusable function. (Reflective from HW2, problem 2.7)


def taxes_owed(price):
    return (price * 0.07) + price


print(taxes_owed(25))


# 2.4. Average function (3 points)
# Write a function that takes three arguments (numerical) and returns the average of the numbers entered.
def avg_func(num1, num2, num3):
    total = 3
    return (num1 + num2 + num3) / total


print(avg_func(1, 10, 100))
