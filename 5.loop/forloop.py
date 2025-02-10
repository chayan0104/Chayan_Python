names_list = ["Alice", "Bob", "Charlie", "David"]
# roll_list=[1,2,3,4]

print("Original List items :" ,",".join(names_list))

# method1
# for name, roll in zip(names_list, roll_list):
#     print(f"The roll no-{roll}'s name is {name}")
    
for i in range(len(names_list)):
    # roll = roll_list[i]
    name = names_list[i]
    # print(f"The roll no-{roll}'s name is {name}")
    print(f"The roll no-{i+1}'s name is {name}")