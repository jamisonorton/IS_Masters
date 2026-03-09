# Exercise #1: (5 points)
# Write a program that generates the following pattern. Use functions to break up the problem into reusable blocks of code.



# Code Example:
# def topOrBottom():
#     print ("#####")
# Output:

# #####
# #      #
#   # #
#    #
#   # #
# #      #
# #####



# Exercise #2: (5 points)
# Write a function that converts a number from feet to inches (12 inches in a foot) and 
# another function that converts feet to meters (0.3048 meters in a foot). 
# Each function should accept a single argument and use that argument to calculate the conversion and print the result. 
# Next, write a program that generates the following output - make sure to use your functions in your program!



# 0 ft:
# ... 0 inches
# ... 0 meters
# 1 ft:
# ... 12 inches
# ... 0.3048 meters
# 2 ft:
# ... 24 inches
# ... 0.6096 meters
# 3 ft:
# ... 36 inches
# ... 0.9144 meters
# 4 ft:
# ... 48 inches
# ... 1.2192 meters
# 5 ft:
# ... 60 inches
# ... 1.524 meters
# 6 ft:
# ... 72 inches
# ... 1.8288 meters
# 7 ft:
# ... 84 inches
# ... 2.1336 meters
# 8 ft:
# ... 96 inches
# ... 2.4384 meters
# 9 ft:
# ... 108 inches
# ... 2.7432 meters




# Exercise #3: (5 points)
# Write a function that rolls two dice. 
# Your function should be designed to accept a single argument (an integer) and generate two die rolls between 
# 1 and the number supplied. Your function should then return the two rolls in ascending order. 
# Next, write a program that rolls 5 sets of dice with different sides. Here's a sample running of your program:



# 6 sided dice roll: 2 & 4
# 7 sided dice roll: 3 & 4
# 8 sided dice roll: 1 & 8
# 9 sided dice roll: 7 & 7
# 10 sided dice roll: 4 & 6 



# Exercise #4: (5 points)
# Guess the number
# Prompt the user to guess a number. Check in input from the user against the secret number that was randomly generated. 
# Limit the guesses to 6 chances. If the user correctly guesses, then print "Good job! You guessed my number in x guesses!" 
# Else, if they failed to guess correctly, print "Nope. The number I was thinking of was x".
# Use the following code to get you started:

# # This is a guess the number game.
# import random
# # use the random.randint() function to generate a random number between 1 and 20.
# secretNumber = random.randint(1, 20)

# print('I am thinking of a number between 1 and 20.')

# guess = 0
# guesses = 0
# # Ask the player to guess 6 times.
# for guessesTaken in range(1, 7):
# ...

# # Sample output:
# # I am thinking of a number between 1 and 20.
# # Take a guess.
# # 4
# # Your guess is too low.
# # Take a guess.
# # 18
# # Your guess is too high.
# # Take a guess.
# # 10
# # Your guess is too low.
# # Take a guess.
# # 15
# # Good job! You guessed my number in 4 guesses!