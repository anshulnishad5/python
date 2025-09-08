class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

result_add = Calculator.add(3, 5)
result_multiply = Calculator.multiply(4, 6)
print(f"Addition Result: {result_add}")
print(f"Multiplication Result: {result_multiply}")


