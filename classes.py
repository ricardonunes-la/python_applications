def main_function():
    # Creating an instance of CustomClass1
    obj1 = CustomClass1()
    obj1.method1()
    obj1.method2("This is a custom string")

    # Creating an instance of CustomClass2
    obj2 = CustomClass2()
    obj2.method1()


class CustomClass1:
    def method1(self):
        # CustomClass1 method 1
        print("Executing method 1 of CustomClass1")

    def method2(self, some_text):
        # CustomClass1 method 2
        print("Executing method 2 of CustomClass1: " + some_text)


class CustomClass2(CustomClass1):
    def method2(self):
        # CustomClass2 method 2
        print("Executing method 2 of CustomClass2")

    def method1(self):
        # CustomClass2 method 1
        super().method1()
        print("Executing method 1 of CustomClass2")


if __name__ == "__main__":
    main_function()
