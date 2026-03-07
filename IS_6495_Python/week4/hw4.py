# Exercise #1: (10 points)
# Fantasy Game Inventory
# You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on. Write a 'for loop' and print out the players inventory. The output should be as below:

# Inventory:
# 1 rope
# 6 torch
# 42 gold coin
# 1 dagger
# 12 arrow
# 3 map fragments
# Total number of items : 65
# Hint: You can use a 'for loop' to loop through all the keys in a dictionary. Use the dictionary below:

stuff = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12,
    "map fragments": 3,
}

print("Inventory: ")
total = 0

for item in stuff:
    count = stuff[item]
    print(count, item)
    total += count

print(f"Total number of items : {count}")

# Exercise #2: (10 points)
# Comma Code
# Say you have a list value like this:
# Write Python code that coverts the list into a string with all the items separated by a comma and a space, with 'and' inserted before the last item. For example, converting the characters list look like this:

# 'Thor, Thanos, Black Panther, Iron Man, Hulk, Batman and Captain America.'

characters = [
    "Thor",
    "Thanos",
    "Black Panther",
    "Iron Man",
    "Hulk",
    "Batman",
    "Captain America",
]

if len(characters) == 0:
    result = ""
elif len(characters) == 1:
    result = characters[0]
else:
    result = ", ".join(characters[:-1]) + " and " + characters[-1]

print(result + ".")


# Exercise #3: (10 points)
# Create a dictionary of technical terms and allow the user to lookup the definitions of these terms from the dictionary. Use the following list for your dictionary:
# You can use the following resource:
# dict = “stores a key/value pair”
# list = “stores a value at each index”
# map = “see dict”
# set = “stores unordered unique elements”

# Based on the user's input, print the term and the definition.
# Make “exit” a term in the dictionary. Prompt the user to enter a term inside a while loop until the user types the word “exit”.

terms = {
    "dict": "stores a key/value pair",
    "list": "stores a value at each index",
    "map": "see dict",
    "set": "stores unordered unique elements",
    "exit": "exit the program",
}
user_input = input(
    "Please type a term to see the definition. terms = dict, list, map, set, or exit to end the application "
).lower()

while user_input != "exit":
    if user_input in terms:
        print(user_input, "=", terms[user_input])
    else:
        print("Sorry, that term isn't in the dictionary.")

    user_input = input("Enter another term or 'exit' to quit: ").lower()


# # Exercise #4: (2 points)
# # Write an expression that would turn the string "Mississippi" into a set of unique letters.
# # set("Parallel") would return set {"P", "a", "e", "l", "r"}

# # You should only write one line of code for this. Do not assign a variable name to the set.
# # Hint: use the set() data type.

print(set("Mississippi"))


# Exercise #5: (2 points)
# Reassign "hello" in this nested list to say "goodbye" instead:

list1 = [1, 2, [3, 4, "hello"]]
list1[2][2] = "goodbye"
print(list1)


# Exercise #6: (3 points)
# Using keys and indexing, grab the "hello" from the following dictionaries:
# 6a.
d = {"simple_key": "hello"}
print(d["simple_key"])

# 6b.
d = {"k1": {"k2": "hello"}}
print(d["k1"]["k2"])
