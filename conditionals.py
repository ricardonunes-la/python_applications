def main():
    number1 = 10
    number2 = 100

    # Check the relationship between the numbers
    result = ""
    if number1 < number2:
        result = "Number 1 is smaller than Number 2"
    elif number1 == number2:
        result = "Number 1 is equal to Number 2"
    else:
        result = "Number 1 is greater than Number 2"

    # Print the result
    print(result)

    # Use a ternary conditional operator for a concise statement
    result = "Number 1 is smaller than Number 2" if number1 < number2 else "Number 1 is greater than or equal to Number 2"
    print(result)

if __name__ == "__main__":
    main()
