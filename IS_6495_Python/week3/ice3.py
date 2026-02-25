#3.1 Adding a Custom Message in a Loop (4.5 points)
# a. Create a list of five different car brands. Use a for loop to print each brand’s name in uppercase.
# b. Modify your program to print a message for each brand.
# Example:
# I would love to drive a {car}.

car_brands = ['BMW', "Mercedes", 'Toyota', 'Nissan', 'Lincoln']
for item in car_brands:
    print(item.upper())

for item in car_brands:
    print(f"I would love to drive a {item}")


#3.2 Find the vowels – for loop (4.5 points)
# Using the 'if' statement and the 'or' operator, write a program that uses the input() function and asks the user for a word or sentence.
# Print the number of vowels in the string that’s returned from the input() function.
# Use the 'or' operator inside the 'if' condition.

# Pseudo code:
# Prompt user for a word or phrase.
# total = 0
# enter 'for' loop:
# for each letter, check if the letter is an 'a,e,i,o or u'. 
# If a match, then +1 to total.
# end loop.
# Print total results.
# Reminder: Comparisons must be on both sides of the operator. i.e. c == 'e'. Cannot be: or 'a' or 'e'...

""" This is using the or operator, but there is a cleaner way to do this.... """
user_input = input("Please enter a word or phrase: ").strip().lower()
total = 0

for c in user_input:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        total += 1

print(total)


# using if c in function
user_input = input("Please enter a word or phrase: ").strip().lower()
total = 0

for c in user_input:
    if c in 'aeiou':
        total += 1

print(total)