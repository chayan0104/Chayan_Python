list1 =[1,2,3,4,5,6]
list2 =[4,5,6,7,8]

# Missing values in list1
missing_in_list1=set(list2).difference(set(list1))
print("Missing values in list1:",missing_in_list1)

# Additional vales in list1
additional_in_list1 = set(list1).difference(set(list2))
print("Additional values in list1:", additional_in_list1)

# Common vales in lists
common_values = set(list1).intersection(set(list2))
print("Common values in both lists:",common_values)
