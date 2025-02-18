# converting list to tuple and time complexcity

test_data=([5,6],[6,7,8,9],[3])


# result=() #blank tuple
# for nos in test_data:
#     new_nos=tuple(nos)
#     result += new_nos
# print(result)    


# ---------------------------------
# new_list = []

# for nos in test_data:
#     new_list.extend(nos)

# # Convert the final list to a tuple
# result = tuple(new_list)
# print(result)

# ---------------------------------
new_list=[]
for number in test_data:
    new_list += number

print(tuple(new_list))

