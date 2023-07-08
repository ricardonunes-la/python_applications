# Function that takes arguments
def print_names(name1, name2):
    # Print the names
    print(name1, "and", name2)

# Function with a default value for an argument
def exponential_power(base, exponent=1):
    # Calculate the power of a number
    result = 1
    for i in range(exponent):
        result *= base
    return result

# Function that returns a value
def calculate_square(x):
    # Calculate the square of a number
    return x * x

# Function with a variable number of arguments
def calculate_total(*numbers):
    # Calculate the sum of multiple numbers
    total = 0
    for num in numbers:
        total += num
    return total

# Define a basic function
def greeting():
    # Print a welcome message
    print("Welcome!")

# Demonstrate a basic function
greeting()

# Demonstrate a function with arguments
print_names("Ronaldo", "Eusébio")

# Calculate the power of a number with a specific exponent
print(exponential_power(2, 3))

# Calculate the square of a number
print(calculate_square(5))

# Calculate the sum of multiple numbers
print(calculate_total(3, 5, 10, 2))
