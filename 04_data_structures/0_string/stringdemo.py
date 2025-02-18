# name =input("Enter something:").upper()
name ="chayan samanta"

# Slicing in string
print(f"Mr.{name[6:14]}")
# --------------------------------------
# Split method
split_name= name.split(" ")
print("Splitted ",split_name)

# --------------------------------------
# Counting character
count = 0
for char in name.upper():
    if char == "A":
     count += 1

# count = name.count("a")
print(f'A in "{name.upper()}" is {count} times')
# ----------------------------------------------
# Replacing

name2 ="Rakesh Roshan"
corrected_name=name2.replace("Rakesh","Hritik")
print("Corrected name is:",corrected_name)