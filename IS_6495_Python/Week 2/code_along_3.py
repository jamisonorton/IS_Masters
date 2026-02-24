import random

"""
pseudo code:
generate 2 random numbers
ask the user what the sum of the generated numbers are
add the sum of the numbers
begin loop
while answer does not equal the sum
check if the user input matches the sum
if correct, then print "correct" and end loop
else, print "incorrect" and primpt the user again
"""

num1 = random.randint(0, 50)
num2 = random.randint(0, 50)

answer = int(input("What is the sum of " + str(num1) + " + " + str(num2) + " "))
num_sum = num1 + num2

if answer == num_sum:
    print("Correct!")

while num_sum != answer:
    print("Incorrect, please try again")
    answer = int(input("What is the sum of " + str(num1) + " + " + str(num2) + " "))

    if answer == num_sum:
        print("Correct!")
        break
