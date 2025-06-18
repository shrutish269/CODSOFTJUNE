# task2.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    print("Welcome to the Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nSelect operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("Enter choice (1/2/3/4): ")

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Invalid choice. Please select from 1 to 4.")

        except ValueError:
            print("Please enter valid numbers.")

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator.")
            break

if __name__ == "__main__":
    main()
