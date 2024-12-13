def simple_calculator():
    print("Welcome to the Simple Calculator!")

    try:
        # Prompt the user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Display operation options
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        # Get user's choice
        operation = input("Enter the operation (1/2/3/4 or +, -, *, /): ").strip()

        # Perform the chosen operation
        if operation in ('1', '+'):
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif operation in ('2', '-'):
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif operation in ('3', '*'):
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif operation in ('4', '/'):
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please select a valid option.")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
simple_calculator()
