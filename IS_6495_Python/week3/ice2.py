#2.1. Shapes (5 points)
# Create a list called shapes and set: shapes = ['rectangle', 'circle'].
# Use append and add a triangle and print the list.
# Use insert and insert "square" and print the list.
# Remove the rectangle item and print.
# Use del on element two and print.

shapes = ['rectangle', 'circle']
shapes.append('triangle')
print(shapes)

shapes.insert(2, 'square')
print(shapes)

shapes.remove('rectangle')
print(shapes)

del shapes[2]
print(shapes)

#2.2. Sorting (5 points)
# Using the sort function, sort this list in numerical order and print it:
ages = [27, 60, 14, 35, 3, 76]

ages.sort()
print(ages)

# Sort the following list in alphabetical order:
names = ['Quinn', 'John', 'Amber', 'Kim']

names.sort()
print(names)
 

# Sort the following list in numerical order and print:
stats = [[3, 2], [1, 2], [1, 1], [3, 1]]

stats.sort()
print(stats)

#2.3. Min-Max (5 points)
# Create a list of numbers from 1 to 20 using range(), then use min(), max(), and sum() functions. Print out the results for each function.

num_list = []

for i in range(1,21):
    num_list.append(i)

print(num_list)

min_num = min(num_list)
max_num = max(num_list)
sum_num = sum(num_list)

print(min_num)
print(max_num)
print(sum_num)