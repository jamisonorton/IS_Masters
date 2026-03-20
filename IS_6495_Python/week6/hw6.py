# # Exercise #1: (6 points)

# # Write a Python program that asks the user to type in a word in English. Determine if that name is one of the most 100 popular English words.
# # Download and use the data file in Canvas called most_popular_words_in_english.txt located in Module 5 and the Files section.

# # Link to required file: week6/most_popular_words_in_english.txt

# # Here's how to get started:

# # Read in the data and print it out (use the sample code below to get started).

# # Next, split the data using the correct separator character (hint: there is a line break between each word).

# # Finally, use the appropriate built-in functions and list methods to determine if the user's word is contained in the list that you generated in the previous step.


# # Sample code, use this to help get you started:

# # try:

# #     # open a file for reading
# #     myvar = open("most_popular_words_in_english.txt", "r")

# # # an error occurred!  handle it here
# # except:
# #     print ("Something went wrong!")

# file_name = "week6/most_popular_words_in_english.txt"

# try:
#     with open(file_name, "r") as file:
#         words = [line.strip().lower() for line in file]

#     while True:
#         user_input = input(
#             "Please put in an english word: (type 'done' to exit) "
#         ).lower()
#         if user_input == "done":
#             break
#         elif user_input in words:
#             print("That is a common word!")
#         else:
#             print("That word is not in the most 100 popular English words.")

# except FileNotFoundError:
#     print("Something went wrong!")


# # Exercise #2: (6 points)

# # Write a security program that prompts the user for a username and a password. Store the username and password into a file named "security.txt"
# # - make sure to store the username and password on separate lines.

# username = input("What is your username? ")
# password = input("What is your password? ")

# file_name = "week6/security.txt"
# try:
#     with open(file_name, "w") as file:
#         file.write(username + "\n")
#         file.write(password + "\n")

# except FileNotFoundError:
#     print("Something went wrong!")


# # Exercise #3: (6 points)

# # Write a program that opens the "security.txt" file you created for the previous programming exercise and read in the username and password stored in the file.
# # Store these values into a series of variables.

# # Next, prompt the user for a username and password using the input function. If the values supplied by the user match the values stored in the file,
# # allow them to continue. Otherwise present an error message.

# file_name = "week6/security.txt"
# try:
#     with open(file_name, "r") as file:
#         lines = file.readlines()
#         username = lines[0].strip()
#         password = lines[1].strip()

#     user_username = input("What is your username? ")
#     user_password = input("What is your password? ")

#     if user_username == username and user_password == password:
#         print("You can continue...")
#     else:
#         print("That is the incorrect username or password!")

# except FileNotFoundError:
#     print("Something went wrong!")


# Exercise #4: (6 points)

# Write a program that opens up a file named "testscores.txt". This file contains the following information in the following format:

# student name
# score1
# score2
# score3
# Read in the values and print out the average score for the student specified in the file along with the student’s name. Use a 'for loop' to traverse the file contents.

# Hint: You will need to deal with the newline character that comes from reading the file. You can use the split() function and use" \n"
# as the delimiter. Or inside the 'for' loop, use the strip() function to clean it up. You can use the isNumeric() function inside the 'for loop'
# to ensure the value is a number to avoid a runtime error after using strip().

file_name = "week6/testscores.txt"

with open(file_name, "r") as file:
    contents = file.read()
    values = contents.split("\n")

values = [item.strip() for item in values if item.strip() != ""]

for i in range(0, len(values), 4):
    student_name = values[i]
    score1 = int(values[i + 1])
    score2 = int(values[i + 2])
    score3 = int(values[i + 3])

    average = (score1 + score2 + score3) / 3
    print(student_name, average)
