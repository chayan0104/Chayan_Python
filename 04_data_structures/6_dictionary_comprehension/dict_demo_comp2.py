# Creating the dictionary directly
name_cost_dict = {"ram": 100, "shyam": 200, "mohan": 300}

# Print the dictionary
print(name_cost_dict)
# print(name_cost_dict.values())

# Using value 
name_cost_dict = {key: value + 50 for key, value in name_cost_dict.items()}

# Using .get() to increment salary by 50
name_cost_dict = {key: name_cost_dict.get(key) + 50 for key in name_cost_dict}

# Print the updated dictionary
print("Post increment salary:", name_cost_dict)