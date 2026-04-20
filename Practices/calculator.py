num1 = float(input("Enter First number: "))
operation = input("Write ur operation: (+, -, *, /): ")
num2 = float(input("Enter Second number: "))

if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Division by zero not possible")
else:
    print("Undefined operation")