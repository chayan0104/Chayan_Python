"""
Question :
Output Should be like below :
State = Bihar OR Department = IT OR State = Karnataka OR Department = Education
and inclue that with query to fetch the data from DB.
"""
# ------------------------------------------------------------------------------------

state_department_dict = [
    {"State": "Bihar", "Department": "IT"},
    {"State": "Maharashtra", "Department": "Health"},
    {"State": "Karnataka", "Department": "Education"}
]

query = """SELECT * 
FROM (
    SELECT e.EmployeeID, e.State, e.Department, e.Salary
    FROM employee e
    INNER JOIN state_department s 
        ON e.State = s.State 
        AND e.Department = s.Department
) AS subquery
WHERE subquery.Salary >= 100000"""

filter_list =[]   # Empty List

for filter in state_department_dict:
    for key, value in filter.items():
         if not (filter["State"] == "Maharashtra" and filter["Department"] == "Health"):
            filter_list.append(f"{key} = {value}")

# print(filter_list)  
seperator1=" OR " 
result= seperator1.join(filter_list)

seperator2=" AND "
print(query+seperator2+result)


