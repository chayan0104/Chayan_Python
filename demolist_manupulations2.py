employee_names = ["Charlie", "David", "Eve", "Alice", "Bob"]

# Original list
print("Original List:", ",".join(employee_names))

# Inserts at specified index
employee_names.insert(1,"Ram")
print("After insert:", ",".join(employee_names))

#Removes and returns a avlue in particular position
popped_item = employee_names.pop(1)
print("After pop (index 3):", ",".join(employee_names), "Popped:", popped_item)

#Removes bt value
employee_names.remove("Bob")
print("After remove (Bob):", ",".join(employee_names))

#Deleting by Index
del employee_names[1]
print("After del (index 1):", ",".join(employee_names))

#Replacing a vaue in particular postion
employee_names[2]="zara"
print("After changing index 2 to Zara:", ",".join(employee_names))

#Spliting sentence
sentence = "Alice, Bob, Charlie"
split_names = sentence.split(",")
print("After split:", split_names)
