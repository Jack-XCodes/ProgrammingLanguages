# JACOB KASUNZU JOHN
# SCT211-0089/2022

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

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
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                result = calculator.add(num1, num2)
            elif user_input == "subtract":
                result = calculator.subtract(num1, num2)
            elif user_input == "multiply":
                result = calculator.multiply(num1, num2)
            elif user_input == "divide":
                result = calculator.divide(num1, num2)

            print("Result:", result)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
