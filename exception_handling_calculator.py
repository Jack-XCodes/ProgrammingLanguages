class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero"

def main():
    calculator = Calculator()

    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input for numbers")
                continue

            if user_input == "divide" and num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                try:
                    if user_input == "add":
                        result = calculator.add(num1, num2)
                    elif user_input == "subtract":
                        result = calculator.subtract(num1, num2)
                    elif user_input == "multiply":
                        result = calculator.multiply(num1, num2)
                    elif user_input == "divide":
                        result = calculator.divide(num1, num2)

                    print("Result:", result)
                except ValueError:
                    print("Error: Invalid input for calculation")
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
