def greet():
    print("Hello, world!")

def get_name():
    name = input("What is your name? ")
    return name

def greet_with_name(name):
    print("It's a pleasure to make your acquaintance, " + name + "!")

def main():
    greet()
    user_name = get_name()
    greet_with_name(user_name)

if __name__ == "__main__":
    main()