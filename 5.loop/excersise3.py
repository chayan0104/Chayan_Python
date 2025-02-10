no_list =[99,55,66,88,22,12,23]
input_no = int(input("Enter a Number: "))
index=0

sorted_list = sorted(no_list)

print("Sorted List",sorted_list)
for number in sorted_list:
    if number>input_no:
        break
    else :
        index = index+1
        
sorted_list.insert(index, input_no)

print("Updated Sorted List:", sorted_list)        
    
    
        
        