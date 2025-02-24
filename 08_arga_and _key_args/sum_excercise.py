# take n no on input and return the sum of it

def total_sum(*input_nos):
    result = sum(input_nos)  # Sum up all the numbers passed as arguments
    print(f"The total sum is: {result}")

# Get input from the user and convert it to a list of integers
numbers = input("Please enter the numbers separated by space: ").split()

# Convert the input strings to integers and pass them to the total_sum function
total_sum(*map(int, numbers))
