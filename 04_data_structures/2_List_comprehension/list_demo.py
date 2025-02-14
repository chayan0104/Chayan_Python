number_list=list(range(10))
# print(number_list)
# even_list=[number for number in range(50) if number%2==0]

even_list=[number for number in number_list if number%2==0]
# print("Even list:",even_list)
print(f"Even list: {" ".join(map(str,even_list))}")


# odd even list creation
new_list=["Even" if number%2==0 else "Odd" for number in number_list]
print(new_list)
# ---------------------------------------------------------------------

words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# ----------------------------------------------------------------------
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(even_squares)

