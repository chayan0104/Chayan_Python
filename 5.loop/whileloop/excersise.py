# Simple Calculator using while loop
while True:
    print("\n1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Exit")
    choice = input("Select operation: ")

    if choice == '5':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid choice. Try again.")
1up