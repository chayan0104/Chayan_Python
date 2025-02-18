
tuple1=(10,2,3,5,6)
tuple2=(3,6,4,3)

new_tuple=()
# print(tuple(zip(tuple1, tuple2)))

min_len = min(len(tuple1), len(tuple2))  #Finding minimunm range

# for i, j in zip(tuple1, tuple2):
for i in range(min_len):
    result = int(tuple1[i] ** tuple2[i]) 
    # result = i**j;
    new_tuple += (result,)  

print(new_tuple) 