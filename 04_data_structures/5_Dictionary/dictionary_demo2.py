emp_dict = {
    "Name":"chayan",
    "Age":27,
    "Address":"Tarakeshwar" 
    }

print("\nEmployee details:",emp_dict)

# Updating address
print("\nUpdating Address:")
emp_dict["Address"]="Kolkata"
print(emp_dict["Address"])  #print the key value address
print("Employee details now:",emp_dict)

# Update method
print("\nUpdate method")
emp_dict.update({"Name":"Chayan Samanta"})
print("Name updated:",emp_dict["Name"])

# Adding job 
print("\nAdding Job:")
emp_dict["Job"]="Software Engineer"
print("Employee details now:",emp_dict)

# print keys values and all values
print("\nprint keys, values  and all values:")
print(emp_dict.keys(),emp_dict.values())
print(emp_dict.items())

# Removing items
print("\nRemoving items:")
del emp_dict["Address"] # Remove item using del
age=emp_dict.pop("Age") # Remove item using pop() and store the value
print("Address got deleted:",emp_dict)
print("Removed age:", age)  # Output: Removed age

# Iterating through a dictionary
print("\nIterating items:")
for key, value in emp_dict.items():
  print(key, ":", value)  # Iterate over key-value pairs

# Using get() to safely access a value
print("\nUsing get() method:")
print(emp_dict.get("Name"))
 
# Copy Dictionary
print("\nCopy Dictionary:")
new_dict_emp = emp_dict.copy()
print(new_dict_emp.items())

# Converting dictionary to list
print("\nConverting Dictionary to List:")
emplist = list(emp_dict.items())
print("As a list",emplist)