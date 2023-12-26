# writing a program which tells about weather

# taking input from user in temperature

temperature = input('Enter temperature(°C) :')
temperature = int(temperature)
if temperature > 30:
    print("It's a hot day! Drink plenty of water.")
elif temperature < 22:
    print("It's a cold day! Wear warm clothes.")
else:
    print("It's a lovely day")

# price of a house is $1M if a buyer has good credit discout 20% otherwise discout 10%
has_good_credit = False
if has_good_credit:
    print("You will pay $800k")
else:
    print("You will pay $900k")

# LOGICAL OPERATOR and or not

if 1 and not 0:
    print("and")
else:
    print("not and")
if 1 or 0:
    print("or")
print(not False)

# comparision operator > < == != etc.

name = input("Enter name: ")

length = len(name)
if length <= 3:
    print("Name must be more than 3 characters")
elif length > 50:
    print("Name cannot be more than 50 characters")
else:
    print("Nice name")
