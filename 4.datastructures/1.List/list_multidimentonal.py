# Creating 2D list
two_d_list=[["ram",100],["sam",222]]

# print a particular id
print(f"Id is {two_d_list[0][1]}")

# Printing the 2D List
print("\n2D List (List is):")
for row in two_d_list:
    name, id = row  # Unpack the row into name and number
    print(f"Name: {name}, id: {id}")
# ------------------------------------------------------------------
# Creating a 3D List
three_d_list = [[[1, 2, 3],[4, 5, 6]],[[7, 8, 9]]]

# Printing the 3D List
print("\n3D List (List of Matrices):")
for matrix in three_d_list:
    for row in matrix:
        print(row)

