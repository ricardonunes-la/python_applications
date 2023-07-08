# Import the math module, which contains features for working with mathematics
import math

# The math module contains lots of pre-built functions
print("The square root of 25 is", math.sqrt(25))

# In addition to functions, some modules contain useful constants 
print("Pi is approximately:", math.pi)

# Calculate the factorial of a number
factorial = math.factorial(8)
print("The factorial of 8 is:", factorial)

# Calculate the logarithm of a number
logarithm = math.log(100, 10)  # Base 10 logarithm of 100
print("The logarithm of 100 to the base 10 is:", logarithm)

# Calculate the sine of an angle in radians
angle = math.radians(60)  # Convert 60 degrees to radians
sine = math.sin(angle)
print("The sine of 60 degrees is:", sine)

# Calculate the ceiling and floor of a number
ceiling = math.ceil(4.2)  # Round up to the nearest integer
floor = math.floor(4.2)  # Round down to the nearest integer
print("The ceiling of 4.2 is:", ceiling)
print("The floor of 4.2 is:", floor)
