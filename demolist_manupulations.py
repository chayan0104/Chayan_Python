employee_names = ["Charlie", "David", "Eve","Alice", "Bob"]

print("original list " + ", ".join(employee_names))

# Sorting list 
employee_names.sort(key=str) # Sort by string representation
print("sorted List ",employee_names)

# or
# print("sorted List ",sorted(employee_names))

