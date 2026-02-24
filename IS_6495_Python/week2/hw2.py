# Exercise 2.1:
# Write a program that asks the user for the value of a coin. Then determine what kind of coin they entered using this information.
# 1 = “Penny”
# 5 = “Nickle”
# 10 = “Dime”
# 25 = “Quarter”
# 50 = “Half dollar”

# Provide a message if you enter any other value that does not match.
# Sample 1:
# Enter a coin value: 1
# That’s a penny!

# Sample 2:
# Enter a coin value: 80
# That’s not a valid coin!

coins = {1: "penny", 5: "nickle", 10: "dime", 25: "quarter", 50: "half dollar"}

coin_value = int(input("Enter a coin value: "))
if coin_value in coins:
    print(f"That's a {coins[coin_value]}!")

else:
    print("Thats not a valid coin!")


# Exercise 2.2:
# Write a program that asks the user for an integer. Report if it's a multiple of 4, a multiple of 3, both, or neither.

answer = int(input("Please give me an integer... "))

if answer % 4 == 0 and answer % 3 == 0:
    print("That is a multiple of 4 and 3")
elif answer % 4 == 0:
    print("That is a multiple of 4")
elif answer % 3 == 0:
    print("That is a multiple of 3")
else:
    print("That is not a multiple of 4 or 3!")


# Exercise 2.3: (2.5 points)
# Write a program that asks the user for their age. If they are 65 or older, they receive a 30% discount. If they are under 18, they get a 15% discount. Otherwise, no discount.
# Ensure you don't allow the user to enter negative values or zero as a price value.

while True:
    try:
        user_age = int(input("What is your age... "))
        if user_age > 0:
            break
        print("Age must be greater than 0... Please try again.")
    except ValueError:
        print("Please enter a whole number.")

if user_age >= 65:
    discount = 0.3
elif user_age < 18:
    discount = 0.15
else:
    discount = 0

print(f"Discount rate: {discount * 100}%")

# Exercise #2.4: (2.5 points)
# Write a program that asks the user to enter a starting number (integer), ending number (integer) and the word "even" or "odd". Then generate a customized print out based on their input.

# Sample:
# Starting number: 5
# Ending number: 15
# Even or Odd?: even

# 6
# 8
# 10
# 12
# 14

starting_number = int(input("Please enter a starting number: "))
ending_number = int(input("Please enter an ending number: "))
even_or_odd = input("Please type 'even' or 'odd' ")

while even_or_odd != "even" and even_or_odd != "odd":
    print(f"You did not type 'even' or ' odd'. Please try again...")
    even_or_odd = input("Please type even or odd ")

if even_or_odd == "even":
    if starting_number % 2 != 0:
        starting_number += 1
else:  # odd
    if starting_number % 2 == 0:
        starting_number += 1
for i in range(starting_number, ending_number + 1, 2):
    print(i)

# Exercise #2.5: (3 points)
# Write a program that asks the user to enter in a number of products (as an integer). Then prompt the user for that number of prices and compute the total cost of all products.

# Sample:
# Enter a number of products: 3
# Enter price for product # 1: 100
# Enter price for product # 2: 200
# Enter price for product # 3: 300
# Total cost: 600

total_num_products = int(input("Enter a number of products: "))
total_cost = 0

for i in range(1, total_num_products + 1):
    price = int(input(f"Enter price for procut #{i}: "))
    total_cost += price

print(f"Total cost: {total_cost}")

# Exercise #2.6: (3 points)
# Write a program that continually asks the user for book prices. Apply a fixed discount of 10% on each book and print the discounted price. Ask if they want to enter another price - if they do, repeat the process; if not, end the program.

fixed_discount = 0.1

while True:
    try:
        book_price = float(input("Please enter a book price (e.g., 12.00): "))
        if book_price <= 0:
            print("Book price must be greater than 0.00")
            continue

    except ValueError:
        print("Please enter a correct dollar amount")
        continue

    discounted_price = book_price * (1 - fixed_discount)
    print(f"Discounted Price : {discounted_price:.2f}")

    again = input("Enter another price? (yes/no) ").strip().lower()
    if again != "yes":
        break


# Exercise #2.7: (3 points)
# Modify Exercise #2.6 so that your program also calculates the total saved from discounts and the total amount spent.


fixed_discount = 0.1
total_saved = 0.00
total_spent = 0.00

while True:
    try:
        book_price = float(input("Please enter a book price (e.g., 12.00): "))
        if book_price <= 0:
            print("Book price must be greater than 0.00")
            continue

    except ValueError:
        print("Please enter a correct dollar amount")
        continue

    discounted_price = book_price * (1 - fixed_discount)
    saved_price = book_price - discounted_price

    print(f"Discounted Price : {discounted_price:.2f}")

    total_saved += saved_price
    total_spent += discounted_price

    again = input("Enter another price? (y/n) ").strip().lower()
    if again != "y":
        break
print(f"Total saved: ${total_saved:.2f}")
print(f"Total spent: ${total_spent:.2f}")

# # Exercise #2.8: (3 points)
# # Write a program that continually asks the user for the capital of a given country until they get it right. Use a static country for simplicity. Print Correct when the capital is guessed correctly.

import random

countries = {
    "Canada": "Ottawa",
    "Japan": "Tokyo",
    "Australia": "Canberra",
}

country = random.choice(list(countries.keys()))
correct = countries[country].strip().lower()

answer = input(f"What is the capital of {country}: ").strip().lower()

while answer != correct:
    print("Incorrect please try again... ")
    answer = input(f"What is the capital of {country}: ").strip().lower()

print("Correct!")

# Exercise #2.9: (3 points)
# Create a program that first generates two random numbers, each ranging from 1 to 10. Then, it asks the user to solve the addition problem formed by these two numbers. If the user answers correctly, congratulate them and terminate the program. However, if the answer is incorrect, the program should ask them to try solving the equation again, continuing this process until they provide the correct answer.

# Pseudo code:
# Generate 2 random numbers, num1, num2.
# Enter while loop
# Prompt the user "what is num1 + num2" equal?
# check the answer, if the input value equals the num1 + num2 then print "Correct!"
# Else, print "Incorrect" and try again.
# End loop.

import random

num1 = random.randint(1, 50)
num2 = random.randint(1, 50)

while True:
    answer = int(input("What is " + str(num1) + " + " + str(num2) + " " + "equal? "))
    if answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Incorrect. Please try again... ")
