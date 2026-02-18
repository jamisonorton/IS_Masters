###### Part 1 ########
# 1. Grocery Budget Tracker (3 points)

# Description:
# Create a program that asks the user for the cost of fruits, vegetables, meats, and dairy products they plan to buy. The program should then calculate the total grocery bill and display it with the dollar sign.

# pseudocode:

# 1.    Prompt the user for the cost of fruits.
# 2.    Prompt the user for the cost of vegetables.
# 3.    Prompt the user for the cost of meats.
# 4.    Prompt the user for the cost of dairy products.
# 5.    Calculate the total sum of all costs entered by the user.
# 6.    Format the total in currency and print the amount of the grocery bill.
fruits = input("What is the cost of the fruits in your cart? ")
vegitables = input("What is the cost of the vegitables in your cart? ")
meats = input("What is the cost of the meats in your cart? ")
dairy_products = input("What is the cost of the dairy products in your cart? ")
total = float(fruits) + float(vegitables) + float(meats) + float(dairy_products)
print(f"The total price of your cart is ${total}")


###### Part 2 ########
# 2. Book Purchase in Euros (3 points)

# Description:
# Create a program that calculates the cost of purchasing books in Euros, converting it to US Dollars. The program should prompt the user to enter the price of a book in Euros and the number of books they want to buy. It should also ask for the current exchange rate from Euros to US Dollars. Finally, it calculates and displays the total cost in US dollars, formatted to two decimal places.

# Use the exchange rate of EUR €1 = $1.08.

# Note: the keystroke for the euro symbol:
# Windows: Using the Numeric Keypad: Hold down the Alt key and type 0128 on the numeric keypad. Release the Alt key, and the Euro symbol should appear. Make sure the Num Lock is on. Or use the character map to copy it.
# macOS: Keystroke: Press Option + Shift + 2 to type the Euro symbol.

# pseudocode:

# 1.    Prompt the user for the price of a book in Euros.
# 2.    Prompt the user for the number of books to purchase.
# 3.    Prompt the user for the current exchange rate from Euros to US Dollars - optional, or use the hardcoded rate from above.
# 4.    Calculate the total cost by multiplying the book price by the number of books and then by the exchange rate.
# 5.    Print the total cost in US dollars, formatted to two decimal places.

book_in_euros = input("What is the price of a book in Euros? ")
books_to_purchase = input("How many books are you going to purchase? ")
exchange_rate = input("EUR €1 = How many usd? (currently its $1.08)")
total = float(book_in_euros) * int(books_to_purchase) * float(exchange_rate)
print(f"The total price of your books are ${total}")
