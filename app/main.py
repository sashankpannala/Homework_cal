class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

def main():
    print("Welcome to the Calculator")
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ")
        if operation == 'exit':
            print("Goodbye!")
            break
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if operation == 'add':
                result = Calculator.add(a, b)
            elif operation == 'subtract':
                result = Calculator.subtract(a, b)
            elif operation == 'multiply':
                result = Calculator.multiply(a, b)
            elif operation == 'divide':
                result = Calculator.divide(a, b)
            else:
                print("Unknown operation")
                continue
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

