"""
Tuples are ordered, immutable (cannot be changed), and allow duplicate elements.
Use case: When you need an ordered collection of items that shouldn't be modified.

Key operations:
Slicing (my_tuple[1:3])
count(), index()
"""
# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana", 3)

# Accessing elements by index
print("First element:", my_tuple[0])  

# Slicing the tuple
print("Sliced tuple (1 to 4):", my_tuple[1:4])  

# Concatenating tuples
tuple2 = (4, 5, 6)
concatenated_tuple = my_tuple + tuple2
print("Concatenated tuple:", concatenated_tuple)  

# Repeating tuple elements
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple) 
# Checking membership
print("Is 'apple' in my_tuple?", "apple" in my_tuple)  
print("Is 5 in my_tuple?", 5 in my_tuple)  

# Finding length of the tuple
print("Length of the tuple:", len(my_tuple))  

# Counting occurrences of an element
print("Count of 3 in my_tuple:", my_tuple.count(3)) 
# Finding the index of an element
print("Index of 'banana':", my_tuple.index("banana"))  

# Iterating over the tuple
print("Iterating over the tuple:")
for item in my_tuple:
    print(item)

# Nested tuple
nested_tuple = (1, (2, 3), 4)
print("Accessing nested tuple:", nested_tuple[1])  
print("Accessing nested tuple element:", nested_tuple[1][0]) 
