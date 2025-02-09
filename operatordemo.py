# Taking two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Initialize the result variables
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division, modulus, and floor division with check for zero
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
    floor_division = num1 // num2
else:
    division = "Cannot divide by zero."
    modulus = "Cannot perform modulus by zero."
    floor_division = "Cannot perform floor division by zero."

# Exponentiation
exponentiation = num1 ** num2

# Print all results at once
print(f"\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
