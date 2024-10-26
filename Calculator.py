# Simple calculator with basic arithmetic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Simple Calculator")
    
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Display operation choices
    print("\nSelect the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter the number corresponding to your choice: ")

    # Perform the selected operation
    if choice == '1':
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
    else:
        print("Invalid choice. Please select a valid operation.")

# Run the calculator
if __name__ == "__main__":
    calculator()
