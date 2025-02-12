employee_names = ["Charlie", "David", "Eve","Alice", "Bob"]

print("original list:" + ",".join(employee_names))

# Sorting list 
# Sort by string representation
# print("sorted List: ",employee_names.sort(key=str))
# or
print("sorted List:",",".join(sorted(employee_names)))

# Reversing the list
# print("Reversed List: ",", ".join(reversed(employee_names)))
# or
# print("Reversed List:", ",".join(employee_names[::-1]))
# or
employee_names.reverse()
print("Reversed List:", "," .join(employee_names))


# Length of List
print("Length of List:",len(employee_names))