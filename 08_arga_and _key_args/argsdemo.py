# Types of arguments :
# 1)positional args--greet(25,"Alice")
# 2)keyword args--greet(age=25, name="Alice")
# 3)default args--def greet(name, age=30);if the keyword is not passed in that case
# 4)*args-- helps to pass a numbers of data
# ----------------------------------------------------------------------------------------------

# Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 25)  

# Keyword Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=25, name="Alice")

# Default Arguments
def greet(name, age, city="New York"):
    print(f"Hello {name}, you are {age} years old and live in {city}.")

greet("Alice", age=25) # city will be called automatically