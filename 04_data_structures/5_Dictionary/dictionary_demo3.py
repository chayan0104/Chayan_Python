employee_dict= {
    "John Doe": "Developer",
    "Jane Smith": "Tester"
}

management_dict = {
    "Alice Johnson": "Manager",
    "Bob Brown": "HR"
}

# Adding two dictionary to one 
employee_dict.update(management_dict)
print(employee_dict)

# Combine dictionary
new_dict_all={**employee_dict,**management_dict}
print(new_dict_all)