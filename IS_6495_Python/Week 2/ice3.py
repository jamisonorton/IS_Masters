# 1 Sum of Positive Numbers (3 points)

total_sum = 0
user_number = int(input("Please put in a number... "))
while user_number != 0:
    if user_number > 0:
        total_sum += user_number
        user_number = int(input("please put in another number... "))
print(f"Total Sum: {total_sum}")

# 2 Temperature Converter (3 points)
# Create a program that continuously prompts the user to enter temperatures in Fahrenheit until they type 'done'. For each temperature entered, the program should calculate its equivalent in Celsius and keep a cumulative total of all temperatures entered (in Celsius). Finally, it should calculate and display the average temperature in Celsius.
# Hint: Since we don't know how many times the loop will execute, it makes the most sense to use a 'while' loop. You will need to prompt the user in 2 different places. Once outside of the loop and again as the last line inside the while loop.

total_temperature = 0
amount_entered = 0
user_input = input("Please enter a temperature in Fahrenheit or 'done' to finish... ")
while user_input != "done":
    user_temperature = float(user_input)
    celsius_temperature = 5 / 9 * (user_temperature - 32)
    total_temperature += celsius_temperature
    amount_entered += 1
    user_input = input("Please enter a temperature in Fahrenheit or 'done' to finish... ")
average_temp = total_temperature / amount_entered
print(f"The average temperature was {average_temp}")