# 1.1 Create Dictionaries (2.5 points)
# Use any names and birthdays you want to create a birthday dictionary that has four entries.  The name is the key and the value is the birth date.
# Print each birth date by using the key to access each entry.

birthday_dict = {
    "Jamison": "August 12, 1994",
    "Jane": "June 19, 1997",
    "Theodore": "September 28, 2021",
    "Tessa": "April 16, 2024",
}
for name in birthday_dict:
    print(birthday_dict[name])


# 1.2 Update Dictionaries (2.5 points)
# Using the dictionary from above, update the last entry and change the birth date to 06/06/1980.

birthday_dict.update({"Tessa": "06/06/1980"})
# print(birthday_dict)


# 1.3 Dictionary With Lists (2.5 points)
# Create a dictionary of the seasons Fall, Spring and Summer where the name of the season is the key and the value is a list of the months in that season. Print the value of "Fall".

seasons = {
    "Fall": ["September", "October", "November"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"],
}
print(seasons["Fall"])


# 1.4 Dictionary Merge (2.5 points)
# Create the same dictionary as in exercise 3 but also create a second dictionary with only the season of Winter.
# Use the dictionary.update method to merge the winter dictionary into the seasons dictionary.  Print the seasons dictionary.

winter_season = {"Winter": ["December", "January", "February"]}

seasons.update(winter_season)
print(seasons)
