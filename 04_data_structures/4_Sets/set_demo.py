"""
Sets are unordered, mutable, and do not allow duplicate elements.
Use case: When you need a collection of unique items and don't care about the order.

Key operations:
add(), remove(), discard(), union(), intersection()
len(), clear(), copy()
"""

# Creating a set
my_set = {1, 2, 3, "apple", "banana", 3}
print("\nOriginal set:", my_set)

# Adding elements
my_set.add("orange")
my_set.update([5, 6, 7])
print("\nSet after adding:", my_set)

# Removing elements
my_set.remove(2)
my_set.discard("banana")
removed_element = my_set.pop()
print(f"\nRemoved element: {removed_element}")
print("\nSet after pop:", my_set)

# Checking membership
print("\nIs 'apple' in my_set?", "apple" in my_set)
print("\nLength of the set:", len(my_set))

# Set Operations
set2 = {7,8, 9, 10, 1}
print("\nog set",my_set)
print("set2",set2)
print("Union:", my_set.union(set2))
print("Intersection:", my_set.intersection(set2))
print("Difference:", my_set.difference(set2))
print("Symmetric Difference:", my_set.symmetric_difference(set2))

# Iteration
for item in my_set:
    print("\n",item)

# Clearing the set
my_set.clear()
print("\nSet after clear:", my_set)
