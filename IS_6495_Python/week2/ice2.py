# 1. Password verification (2 points)

password = "password1234"
user_password = input("Please enter your password... ")
if user_password == password:
    print("Access Granted")
else:
    print("Access Denied")

# 2. Voting Age (2 points)

voting_age = 18
user_age = int(input("What is your age? "))
if user_age >= voting_age:
    print("You can vote today!")
else:
    years_remaining = voting_age - user_age
    print(f"You have {years_remaining} years until you can vote.")

# 3. Dress for Weather (2 points)

user_temperature = int(input("What is the temperature? "))
if user_temperature < 40:
    print("Wear a warm coat.")
elif user_temperature < 70:
    print("Wear a light jacket.")
elif user_temperature < 100:
    print("Wear something cool.")
elif user_temperature > 100:
    air_conditioning = input("Do you have air conditioning at home? (yes/no) ")
    if air_conditioning == "yes":
        print("Stay at home.")
    else:
        print("Bummer, try a swimming pool.")
