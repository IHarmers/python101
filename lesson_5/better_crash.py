number_one = "Hello"  # Try changing this to a number
number_two = 30

try:
    sum = number_one + number_two
except TypeError:
    print("Please ensure both variables contain numbers")
else:
    print(sum)
