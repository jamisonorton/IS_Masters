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

# Pseudo code:
# 1.    Create variables to hold the total temperature in Celsius and the count of temperatures entered.
# 2.    Prompt the user to enter a temperature in Fahrenheit or 'done' to finish.
# 3.    Enter a loop, while the input is not equal to "done".
#       Convert the input to a float value (the temperature in Fahrenheit).
#       Calculate the equivalent temperature in Celsius.
#       Add the temperature in Celsius to the total variable.
#       Increment the count of temperatures.
#       Prompt the user to enter the next temperature or 'done'.
# 4.    After exiting the loop, calculate the average temperature in Celsius.
# 5.    Format and display the average temperature to the user.
# 6.    End the program.
