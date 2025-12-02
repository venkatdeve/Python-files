
# Functions of add , subtract , multiply , divide
def add(a, b):
    return a + b  # Add


def subtract(a, b):
    return a - b  # Subtraction


def multiply(a, b):
    return a * b  # Multiplication


def divide(a, b):
    # To check zero division error
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Calculator while run  until loop exit
while True:
    # Ask user for input (operation or exit)
    choice = input("Enter operation (+, -, *, /) or 'exit' to quit: ")

    # Exit condition
    if choice.lower() == "exit":
        print("Calculator exited !")
        break

    # Get numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Step 4: Perform the chosen operation
    if choice == "+":
        result = add(num1, num2)
    elif choice == "-":
        result = subtract(num1, num2)
    elif choice == "*":
        result = multiply(num1, num2)
    elif choice == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue  # Restart loop

    # Step 5: Print the result
    print("Result: ",result)