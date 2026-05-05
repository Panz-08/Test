def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Cannot divide by zero")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator")
                continue
            print(f"Result: {result}")
            again = input("Do another calculation? (y/n): ")
            if again.lower() != 'y':
                break
        except ValueError:
            print("Invalid input")

calculator()

