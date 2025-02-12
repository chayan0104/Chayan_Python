
employee_list = ["manish", "Satish", "Rakesh", "Sukriti"]

print("Original list:" + ", ".join(employee_list))

employee_list.append("Ramesh")
employee_list.insert(0,"Suresh")
print("New List :"+ "," .join(employee_list))

print("For a particular employee:",employee_list[0])


print("Will print all after index 2:"+ "," .join(employee_list[2:]))
print("Will print in between:"+ "," .join(employee_list[1:3]))