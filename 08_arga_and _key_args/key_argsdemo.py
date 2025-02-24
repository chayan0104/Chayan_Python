# key args --  keyword arguments (**kwargs) in a function

def person_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
person_info(name="Alice", age=30, occupation="Engineer", city="New York")
