list1 =[1,2,3,4,5,6]
list2 =[4,5,6,7,8]
list3 =[5,6,9,10,11,12]

# common in all list
common_items=(set(list1).intersection(set(list2))).intersection(set(list3))

print("Common items:",common_items)


