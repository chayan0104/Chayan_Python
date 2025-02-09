# int(): Converts to an integer.
# float(): Converts to a float.
# str(): Converts to a string.
# list(): Converts to a list.
# tuple(): Converts to a tuple.
# set(): Converts to a set.

# Initialize variables
str_number = "25"  # string
int_number = 50    # integer
float_number = 12.99  # float
my_list = ['a', 'b', 'c']  # list of characters

# Perform typecasting operations
num = int(str_number)  # string to integer
num_float = float(int_number)  # integer to float
num_int = int(float_number)  # float to integer
list_str = ''.join(my_list)  # list to string

# Print results
print(f"String to integer: {num}")
print(f"Integer to float: {num_float}")
print(f"Float to integer: {num_int}")
print(f"List to string: {list_str}")
