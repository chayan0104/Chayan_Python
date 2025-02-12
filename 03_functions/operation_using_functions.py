# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for division
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."

# Function for modulus
def modulus(num1, num2):
    if num2 != 0:
        return num1 % num2
    else:
        return "Cannot perform modulus by zero."

# Function for floor division
def floor_divide(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return "Cannot perform floor division by zero."

# Function for exponentiation
def exponentiate(num1, num2):
    return num1 ** num2

# Taking two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing all operations and printing the results
print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
print(f"Division: {num1} / {num2} = {divide(num1, num2)}")
print(f"Modulus: {num1} % {num2} = {modulus(num1, num2)}")
print(f"Floor Division: {num1} // {num2} = {floor_divide(num1, num2)}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiate(num1, num2)}")
