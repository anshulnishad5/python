def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    result = divide(a, b)
    if result is not None:
        print(f"Result: {result}")
except ValueError:
    print("Please enter valid integers.")

