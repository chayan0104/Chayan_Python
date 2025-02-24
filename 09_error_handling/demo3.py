input_no_1 = input("Please enter the first number: ")
input_no_2 = input("Please enter the second number: ")

# input ---- xyz , 123 , 0 will cause error 
try:
    division = input_no_1 / input_no_2
    remainder = input_no_1 % input_no_2
    print(f"Division result is {division} and remainder is {remainder}")

except (ZeroDivisionError,ValueError) as e:
    print(f"Error:{e}")

finally:
    print("Operation finished")
