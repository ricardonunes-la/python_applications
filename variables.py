# Declare and initialize a variable
f = 0
print(f)

# Re-declaring the variable
f = "abc"
print(f)

# ERROR: Combining variables of different types
#print("string type " + 123)
print("string type " + str(123))

# Global vs. local variables in functions
def someFunction():
    # global f
    f = "def"
    print(f)

someFunction()
print(f)

# Delete the variable
del f
# Attempting to print a deleted variable
# print(f) - This would cause an error as the variable no longer exists
