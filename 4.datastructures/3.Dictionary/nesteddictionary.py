# Create a nested dictionary
emp_dict = {
    "Name": "Chayan",
    "Age": 27,
    "Address": {
        "City": "Tarakeshwar",
        "State": "West Bengal",
        "Country": "India"
    },
    "Job": {
        "Title": "Software Engineer",
        "Department": "IT",
        "Experience": "4 years"
    }
}

# Print the nested dictionary
print(emp_dict)

# Accessing nested dictionary elements
print("Name:",emp_dict["Name"])
print("City:",emp_dict["Address"]["City"])
print("Job Experience:",emp_dict["Job"]["Experience"])

