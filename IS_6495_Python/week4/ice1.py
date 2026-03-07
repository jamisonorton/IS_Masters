# 4.1. Split Number List (2.5 points)
# Use the string.split method create a list of numbers from the following string and then print the list to the screen.
my_list = "10 67 123 46 20 18 36 250"
split_list = my_list.split()
print(split_list)


# Do the same thing for this string:
new_list = "10,67,123,46,20,18,36,250"
new_split = new_list.split(",")
print(new_split)


# 4.2 Split Data into List (2.5 points)
# Use the string.split method create a list of numbers from the following string and then sum up the numbers.  Print the sum to the screen.
string_list = "90,67,87,102,77,80"
num_split = [int(x) for x in string_list.split(",")]
print(sum(num_split))


# 4.3 Slice Lists (2.5 points)
# Use the slicing syntax of lists to get the first 4 numbers in the following list and print out the results.
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_four = list_a[0:4]
print(first_four)


# 4.4 Slice Lists with Increment (2.5 points)
# Use the slicing syntax of lists to get every other entry in the following list starting at the beginning and print the results.

# Sample output:
# ['a', 'c', 'e', 'g']

list_b = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = list_b[0::2]
print(sliced_list)
