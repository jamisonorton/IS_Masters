# 1. Exception handling (5 points)

# Write a loop that uses a try except else block to verify that the user entered a valid (integer) number.  The loop should run until a valid number has been entered.
while True:
    try:
        user_input = int(input("Please input an integer: "))
    except ValueError:
        print("That is not an integer. Please try again!")
    else:
        print("Thank you!")
        break

# 2. File IO (5 points)

# Write a program that opens a file that will be overwritten each time.  Write out a few lines of text and then close the file.
while True:
    file_name = input("Enter a file name: ")
    try:
        with open(file_name, "w") as file:
            file.write("I am writing a line\nand putting a new line." + "\n")
            file.write("I need more dummy text..." + "\n")
        break

    except Exception as ex:
        print(ex)

# 3. Name (5 points)

# Write a program that prompts the user for a file name.  If the file exists, open it and print each line.  If the file does not exist,
# handle the open file exception and print a message stating that the file was not found.
while True:
    file_name = input("Enter a file name: ")
    try:
        with open(file_name, "r") as file:
            for line in file:
                print(line, end="")
        break

    except FileNotFoundError:
        print("File was not found.")
