# try:: Code you think might fail.
# except:: What happens if an error occurs.
# else:: Runs if no error happens.
# finally:: Always runs, whether an error occurs or not (used for cleanup).

# ZeroDivisionError-------------------------------------------
try:
    result = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Error: Can't divide by zero!")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise IndexError
except IndexError:
    print("Error: Index out of range!")

# ValueError-------------------------------------------------
try:
    num = int("abc")  # This will raise ValueError
except ValueError:
    print("Error: Invalid value to convert!")

# TypeError------------------------------------------------------
try:
    result = "string" + 5  # This will raise TypeError
except TypeError:
    print("Error: You can't combine a string and a number!")

# FileNotFoundError----------------------------------------------------------
try:
    file = open("non_existent_file.txt", "r")  # This will raise FileNotFoundError
except FileNotFoundError:
    print("Error: File not found!")
