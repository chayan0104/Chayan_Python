# Taking two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
addition = num1 + num2
print(f"Addition: {num1} + {num2} = {addition}")

# Subtraction
subtraction = num1 - num2
print(f"Subtraction: {num1} - {num2} = {subtraction}")

# Multiplication
multiplication = num1 * num2
print(f"Multiplication: {num1} * {num2} = {multiplication}")

# Division
if num2 != 0:
    division = num1 / num2
    print(f"Division: {num1} / {num2} = {division}")
else:
    print("Division: Cannot divide by zero.")

# Modulus (remainder of division)
if num2 != 0:
    modulus = num1 % num2
    print(f"Modulus: {num1} % {num2} = {modulus}")
else:
    print("Modulus: Cannot perform modulus by zero.")

# Floor Division (integer division)
if num2 != 0:
    floor_division = num1 // num2
    print(f"Floor Division: {num1} // {num2} = {floor_division}")
else:
    print("Floor Division: Cannot perform floor division by zero.")

# Exponentiation (power)
exponentiation = num1 ** num2
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
