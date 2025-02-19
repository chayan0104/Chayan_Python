"""
Question :
Output Should be like below :
State = Bihar OR Department = IT OR State = Karnataka OR Department = Education
"""
# ------------------------------------------------------------------------------------

state_department_dict = [
    {"State": "Bihar", "Department": "IT"},
    {"State": "Maharashtra", "Department": "Health"},
    {"State": "Karnataka", "Department": "Education"}
]

filter_list =[]   # Empty List

for filter in state_department_dict:
    for key, value in filter.items():
         if not (filter["State"] == "Maharashtra" and filter["Department"] == "Health"):
            filter_list.append(f"{key} = {value}")

# print(filter_list)   

print(" OR ".join(filter_list))


