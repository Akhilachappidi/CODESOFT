def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter the operation number (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input! Please choose a valid operation.")
        return

    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(n1, n2)
    elif choice == '2':
        result = subtract(n1, n2)
    elif choice == '3':
        result = multiply(n1, n2)
    else:
        result = divide(n1, n2)

    print("Result: ", result)

if __name__ == "__main__":
    calculator()
