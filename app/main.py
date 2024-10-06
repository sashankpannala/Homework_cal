class Calculator:
    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator.history.append(f"Added {a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator.history.append(f"Subtracted {a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append(f"Multiplied {a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero")
        result = a / b
        Calculator.history.append(f"Divided {a} / {b} = {result}")
        return result

    @classmethod
    def get_last_calculation(cls) -> str:
        if cls.history:
            return cls.history[-1]
        return "No calculations performed yet."

    @classmethod
    def clear_history(cls):
        cls.history.clear()

