"""Lists:
Description: Lists are ordered, mutable (can be changed), and allow duplicate elements.
Use case: When you need an ordered collection of items, and the items can be changed.

Key operations:
append(), insert(), remove(), pop(), extend()
len(), sort(), reverse()
"""
employee_list = ["manish", "Satish", "Rakesh", "Sukriti"]

print("Original list:" + ", ".join(employee_list))

employee_list.append("Ramesh")
employee_list.insert(0,"Suresh")
print("New List :"+ "," .join(employee_list))

print("For a particular employee:",employee_list[0])


print("Will print all after index 2:"+ "," .join(employee_list[2:]))
print("Will print in between:"+ "," .join(employee_list[1:3]))