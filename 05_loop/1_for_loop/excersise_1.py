# Star pattern
star = "* "

for i in range(5):
    print(star * (i+1))
    
# Finding even no
even_list = []

for number in range(1,20):
     if number % 2 == 0:
        even_list.append(number)
              
print("Even numbers are:",even_list)

# Inverted start pattern
n = 5  
star2= "* "

for i in range(n, 0, -1):  # Loop from n down to 1
    for j in range(i, 0, -1):  # Print numbers from i down to 1
        print(star2, end="")
    print()  # New line after each row
