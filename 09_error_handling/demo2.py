# custom error and multiple error

try:
    result = 10 / 0  # ZeroDivisionError
    sum = "Abc"+ 123  #TypeError
    num = int("abc")  # ValueError

# Custom error message
except(ZeroDivisionError,TypeError,ValueError) as e:
    print(f"An error occurred: {e}")  #first error occurs will be print, others will not be executed
