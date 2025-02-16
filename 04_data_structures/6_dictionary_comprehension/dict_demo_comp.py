# Genenal Structure
# {key_expression: value_expression for item in iterable if condition}

# list to dictionary making

name_list=["Ram","Shyam","Ramu"]
cost_list=[100,120,65,8979]

new_dict={name_list[i]: cost_list[i] for i in range(len(name_list))}

print(new_dict)