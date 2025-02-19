
names=["Ram","Sam","Raj"]

joined_names = " ".join(names)

print(joined_names)
print("-".join(names))
print(",".join(names))
# --------------------------------------

numbers={1,2,3,4,6}

final_output=""

for num in map(str,numbers):
    final_output += (num +",")

# print(final_output.rstrip(",")) 
print(final_output.removesuffix(",")) 
   
# or just using join 

# map(function, iterable)
print(",".join(map(str, numbers)))