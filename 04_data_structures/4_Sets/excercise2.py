list1 =[1,2,3,4,5,6]
list2 =[4,5,6,7,8]
list3 =[5,6,9,10,11,12]

#Common in all list
common_items=(set(list1).intersection(set(list2))).intersection(set(list3))

print("Common items:",common_items)

# ----------------------------------------------
# Initialize an empty list to store common items
common_items = []

# Loop through each item in list1 and check if it exists in list2 and list3
for item in list1:
    if item in list2 and item in list3:
        common_items.append(item)

print("Common items:", common_items)