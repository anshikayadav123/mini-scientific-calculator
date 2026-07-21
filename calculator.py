import math

# Basic operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Advanced operations
def square_root(x): return math.sqrt(x)
def power(x, y): return math.pow(x, y)
def percentage(x, y): return (x / y) * 100
def modulus(x, y): return x % y

# Scientific operations
def sine(x): return math.sin(math.radians(x))
def cosine(x): return math.cos(math.radians(x))
def tangent(x):
    if x % 180 == 90:
        return "Error! Tangent undefined at 90°, 270°..."
    return math.tan(math.radians(x))
def logarithm(x): 
    if x <= 0:
        return "Error! Logarithm undefined for non-positive numbers."
    return math.log(x)
def factorial(x): 
    if x < 0:
        return "Error! Factorial not defined for negative numbers."
    return math.factorial(int(x))

def calculator():
    while True:
        print("\n--- Mini Scientific Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power (x^y)")
        print("7. Percentage (x out of y)")
        print("8. Modulus (x % y)")
        print("9. Sine (sin x)")
        print("10. Cosine (cos x)")
        print("11. Tangent (tan x)")
        print("12. Logarithm (ln x)")
        print("13. Factorial (x!)")
        print("14. Exit")

        choice = input("Enter choice (1-14): ")

        if choice == '14':
            print("Exiting Calculator... Goodbye!")
            break

        # Single-input operations
        if choice in ['5','9','10','11','12','13']:
            num = float(input("Enter number: "))
            if choice == '5':
                print("Result:", square_root(num))
            elif choice == '9':
                print("Result:", sine(num))
            elif choice == '10':
                print("Result:", cosine(num))
            elif choice == '11':
                print("Result:", tangent(num))
            elif choice == '12':
                print("Result:", logarithm(num))
            elif choice == '13':
                num = int(num)
                print("Result:", factorial(num))

        # Two-input operations
        elif choice in ['1','2','3','4','6','7','8']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '6':
                print("Result:", power(num1, num2))
            elif choice == '7':
                print(f"{num1} is {round(percentage(num1, num2), 2)}% of {num2}")
            elif choice == '8':
                print("Result:", modulus(num1, num2))
        else:
            print("Invalid Input! Please try again.")

# Run calculator
calculator()
