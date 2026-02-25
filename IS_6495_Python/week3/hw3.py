# Exercise 1: (3 points)
# Given the list below, write a program that counts the # of A’s (scores between 90 and 100). Extension: Count the # of B’s, C’s, D’s and F’s.
# Hint: use an if-elif-else condition inside a for loop.

grades = [90,100,70,45,76,84,93,21,36,99,100]
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

for item in grades:
    if item in range(90,101):
        count_a += 1
    elif item in range(80,90):
        count_b += 1
    elif item in range(70,80):
        count_c += 1
    elif item in range(60,70):
        count_d += 1
    else:
        count_f += 1
print(count_a)
print(count_b)
print(count_c)
print(count_d)
print(count_f)
 


# Exercise 2: (3 points)
# Given the following list of student test scores, apply a class "curve" to each score. The class curve is as follows:
# 90 or above: no curve
# 80 to 90: +2 points
# 70 to 80: +5 points
# Lower than 70: +8 points
# Use the below test scores list:

grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]

new_grades = grades.copy()

# Pseudo code: for each score in list,
# If grade is greater than or equal to 90, move on to next score.
# Else if score is greater or equal to 80 but less than 90, add 2 points.
# Else if score is greater or equal to 70 but less than 80, add 5 points.
# Else, add 8 points
# Print out the new grades.

for i in range(len(new_grades)):
    if new_grades[i] in range(90,101):
        continue
    elif new_grades[i] in range(80,90):
        new_grades[i] += 2
    elif new_grades[i] in range(70,80):
        new_grades[i] += 5
    else:
        new_grades[i] += 8

print(new_grades)


# Exercise 3: (3 points)
# Write a program that asks the user for daily sales figures for a full week (Sunday – Saturday). 
# Store these values in a list and print them out at the end of your program. Here's a sample running of your program:
# Enter sales for Day #1: 100
# Enter sales for Day #2: 200
# Enter sales for Day #3: 300
# Enter sales for Day #4: 400
# Enter sales for Day #5: 500
# Enter sales for Day #6: 600
# Enter sales for Day #7: 700
# Sales for the week: [100,200,300,400,500,600,700]

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 

sales = []

for i in range(len(days)):
    user_input = int(input(f"Enter sales for {days[i]}: "))
    sales.append(user_input)

print(sales)    


# # Exercise #4: (3 points)
# # Given the following list, write a program that does the following:
# # Extract the first 3 elements of the list into a new list
# # Extract the characters b, c, and d into a new list
# # Extract the last 4 characters into a new list

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

first_three = my_list[:3]
print(first_three)

bcd = my_list[1:4]
print(bcd)

last_four = my_list[3:]
print(last_four)

 

# Exercise #5: (3 points)
# Given the following lists, write a program that lets the user type in the name of a product. 
# If the product name exists in our inventory, you should print out that it is in our inventory. 
# Otherwise you should print out that the product is not found. Ensure that your program is case insensitive (i.e. searches for "Apple" or "apple" or "APPLE" should all succeed).

products = ["apple", "pear", "peach", "banana"]

user_input = input("Please enter a product: ").strip().lower()

if user_input in products:
    print("This product already exists in our inventory.")
else:
    print("Product not found")

 

# Exercise #6: (3 points)
# Given these two lists, write a program that finds all elements that exist in both lists (i.e. the integer 2 exists in both lists). 
# Store your results in a list and print it out to the user. 
# The expected answer is: [1, 2, 3]
# Two lists:

a = [1,2,3,4,5]

b = [2,3,10,11,12,1]

c = []

# using for loop....
for x in a:
    if x in b:
        c.append(x)

print(c)

# the real fun way...
overlap = sorted(list(set(a) & set(b)))
print(overlap)



# Exercise #7: (3 points)
# Write a program that continually prompts a user to enter in a series of first names. 
# The user can elect to stop entering names when they supply the string "end." Store these first names in a list and print them out at the end of your program. 
# Extension: Prevent the user from entering duplicate names (hint: use the in operator).

names = []

while True:
    user_input = input("Please put in a first name: (type 'end' to exit) ").strip()

    if user_input.lower() == 'end':
        break

    name = user_input.capitalize()

    if name in names:
        print("That name is already in the list")
        continue
    
    names.append(name)
    
print(names)



# Exercise #8: (3 points)
# Continually ask the user for a product name. Next, see if that product name is included in the inventory list below. 
# If it is, remove the product from the list and then print the current list of products to the user. 
# If the product is not on the list you should alert the user that we do not currently carry the product in question. 
# You can end the program when the list of products is exhausted or when the user types the string "end." 

products = ["apple", "pear", "peach", "banana"]

while products:
    user_input = input("Please enter a product: (type end to exit | Remove all products from inventory) ").strip().lower()

    if user_input == 'end':
        break

    if user_input in products:
        products.remove(user_input)

        if products:
            print("Current inventory", products)
        else:
            print("Inventory Exausted")
    else:
        print("We do not currently carry that product...")
    
    

# Exercise #9: (3 points)
# The lists below are organized in such a way that the item at position 0 in the first list matches with the item at position 0 in the second list. 
# With this in mind, write a product price lookup program that works as follows:
# Enter a product:  peanut butter
# This product costs 3.99

products = ['peanut butter', 'jelly', 'bread']

prices = [3.99, 2.99, 1.99]

price_lookup = dict(zip(products, prices))

while True:
    user_input = input("Please enter a product: (type end to exit) ").strip().lower()

    if user_input == 'end':
        break

    if user_input in price_lookup:
        print(f"This product costs {price_lookup[user_input]}")
    else:
        print("Product not found")

 

# Exercise #10: (3 points)
# Write a program that asks a teacher for the number of students in his or her class. 
# Next, ask the teacher how many assignments are given in this class. With this information prompt the user to enter in scores for each student and compute their average grade in the class.
# Hint: use a nested for loop for the assignments inside the student for loop. (For each student, iterate for each assignment)

# Sample:
# (Input sample)
# How many students in the class? 2
# How many assignments in the class? 2

# (Output sample)
# Student #1
# Assignment #1: 100
# Assignment #2: 90
# Student #1 earned a 95

# Student #2
# Assignment #1: 90
# Assignment #2: 80
# Student #2 earned a 85

# Input

student_count = int(input("How many students in the class? "))
assignment_count = int(input("How many assignments in the class? "))

# Output

for s in range(student_count):
    print(f"\nStudent #{s + 1}")

    total = 0

    for a in range(assignment_count):
        grade = int(input(f"Assignment #{a + 1}: " ))
        total += grade
    
    average = total / assignment_count

    print(f"Student #{s + 1} earned a {int(average)}")