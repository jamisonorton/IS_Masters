#1.1. Creating and Modifying a List (2.5 points)
# Create a list of four different sports of your choice, modify it by adding and removing elements, and print the updated list.

# sports = ['Ultimate Frisbee', 'Soccer', 'Basketball', 'Football']
# sports.append('Rugby')
# print(sports)

# sports.remove('Football')
# print(sports)

# greatest_sport = sports.pop(0)
# print(greatest_sport)

# print(sports)


#1.2. Copying and Modifying Lists (2.5 points)
# Create a list of five different desserts of your choice. Copy the list of desserts to a new list, modify both lists separately, and print both.

desserts = ['Cake', 'Ice Cream', 'Chocolate', 'Cookies', 'Pie']

new_desserts = desserts.copy()

desserts.insert(2, 'Doughnut')
new_desserts.remove('Cake')

print(desserts)
print(new_desserts)
