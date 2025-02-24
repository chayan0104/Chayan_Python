input_no_1 = input("Please enter the first number: ")
input_no_2 = input("Please enter the second number: ")

# input ---- xyz and  0 will cause error 
try:
    input_no_1 = float(input_no_1)
    input_no_2 = float(input_no_2)

    division = input_no_1 / input_no_2
    remainder = input_no_1 % input_no_2
    
except (ZeroDivisionError,ValueError) as e:
    print(f"Error:{e}")

else:
    print(f"Division result is {division} and remainder is {remainder}")

finally:
    print("Operation finished")
