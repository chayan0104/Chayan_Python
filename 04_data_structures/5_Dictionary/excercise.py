employee_directory = {
    "EMP001": {"name": "John Doe", "age": 29, "department": "IT", "position": "Software Engineer"},
    "EMP002": {"name": "Jane Smith", "age": 35, "department": "HR", "position": "HR Manager"},
    "EMP003": {"name": "Alice Johnson", "age": 27, "department": "Finance", "position": "Accountant"}
}

# Add a new employee to the directory.
employee_directory["EMP004"] = {"name": "James anderson", "age": 24, "department": "Devops", "position": "Jr devops"}
print(employee_directory["EMP004"])

# Update an employee's details (e.g., update the age or position).
employee_directory["EMP002"]["age"]=32
print(employee_directory["EMP002"]["age"])

# Remove an employee from the directory using their ID.
del employee_directory["EMP003"]
print(employee_directory.items())

# Print the details of an employee using their ID.
print(employee_directory["EMP001"])

# Print the entire employee directory at the end to check the final state.
print("Complete Directory of employees:",employee_directory)

for i in range(len(employee_directory["EMP003"])):
    print((employee_directory["EMP003"]["name"]))
    break