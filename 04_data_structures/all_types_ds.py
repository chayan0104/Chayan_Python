# 1. List
# A list is an ordered collection of elements that can be changed, modified, and allows duplicates.
my_list = [1, 2, 3, 3, "apple", "banana"]  # List with elements
print(f"List with elements: {my_list}")
# Features: Mutable, ordered, can store any data type, allows duplicates.

# 2. Tuple
# A tuple is an ordered collection like a list, but it is immutable (cannot be changed after creation).
my_tuple = (1, 2, 3, 3, "apple", "banana")  # Tuple with elements
print(f"Tuple with elements: {my_tuple}")
# Features: Immutable, ordered, can store any data type, allows duplicates.

# 3. Set
# A set is an unordered collection of unique elements. It does not allow duplicates.
my_set = {1, 2, 3, 3, "apple", "banana"}  # Set with elements
print(f"Set with elements: {my_set}")
# Features: Immutable (set operations), unordered, no duplicates.

# 4. Dictionary
# A dictionary is a collection of key-value pairs, where keys must be unique.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}  # Dictionary with key-value pairs
print(f"Dictionary with elements: {my_dict}")
# Features: Mutable, unordered, key-value pairs, keys are unique, values can be any data type.

# 5. Frozenset
# A frozenset is similar to a set but immutable.
my_frozenset = frozenset([1, 2, 3, 3, "apple", "banana"])  # Frozenset with elements
print(f"Frozenset with elements: {my_frozenset}")
# Features: Immutable, unordered, no duplicates, does not allow modification after creation.
