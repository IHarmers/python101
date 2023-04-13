
# Basic if statements
#
# Execute an operation if certain conditions are met.
#

happy = True  # Try changing this to True

if happy == True:
    print(":)")

if happy != True:
    print(":(")

# if-else statements

drink = "Fanta"  # Try changing this to values like: "Beer", "Fanta" or "Fristi"
soft_drinks = ["Cola", "Pepsi", "Sprite", "Fanta"]

if drink == "Water":
    print("Water is very healthy. Good choice!")
elif drink == "Tea":
    print("Tea makes you feel warm inside")
elif drink == "Beer" or drink == "Wine":
    print("Don't drink too much or you will get drunk")
elif drink in soft_drinks:
    print("These drinks contain a lot of sugar")
else:
    print("I don't know this drink, but I bet it's delicious!")

# While loops
#
# Repeat an operation while a certain condition
# is not met.
#

# Try setting different numbers for these counters
current_count = 8
maximum_count = 10

while current_count <= maximum_count:
    print("The current count is {}".format(current_count))
    current_count = current_count + 1

# For loops
#
# Repeat an operation for every element in a collection
#

# Try adding and removing items from the list
checklist = ["Clothes", "Tent", "Shoes", "Drinks","Marshmellows", "Pizza!"]

print("Things to bring on a camping trip:")

for item in checklist:
    print("- {}".format(item))
