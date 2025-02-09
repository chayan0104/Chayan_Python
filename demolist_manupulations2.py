employee_names = ["Charlie", "David", "Eve", "Alice", "Bob"]

# Original list
print("Original List:", ",".join(employee_names))

# Inserts an element at the specified index
employee_names.insert(1,"Ram")
print("After insert:", ",".join(employee_names))

# Removes and returns the element at the specified index (default is the last item)
popped_item = employee_names.pop(1)
print("After pop (index 3):", ",".join(employee_names), "Popped:", popped_item)

# #Removes the first occurrence of the specified value
employee_names.remove("Bob")
print("After remove (Bob):", ",".join(employee_names))

# #Deletes the item at a specific index or the entire list
del employee_names[1]
print("After del (index 1):", ",".join(employee_names))

# #Change an item in the list** - Modify an element at a specific index
employee_names[2]="zara"
print("After changing index 2 to Zara:", ",".join(employee_names))

# #This works on strings, but I'll show an example here.
sentence = "Alice, Bob, Charlie"
split_names = sentence.split(",")
print("After split:", split_names)
