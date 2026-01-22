def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by Zero is not possible"
    return a / b

def calc():
    print("Simple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        Arithmetic_Operation = input("Arithmetic Operation (+, -, *, /): ").strip()

        if Arithmetic_Operation == '+':
            result = addition(num1, num2)
        elif Arithmetic_Operation == '-':
            result = subtraction(num1, num2)
        elif Arithmetic_Operation == '*':
            result = multiplication(num1, num2)
        elif Arithmetic_Operation == '/':
            result = division(num1, num2)
        else:
            print("Invalid operation. Please use +, -, *, / only.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calc()
