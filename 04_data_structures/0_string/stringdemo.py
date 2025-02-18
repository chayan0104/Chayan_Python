name =input("Enter something:").upper()

count =[]
for char in name.upper():
    if char=="A":
     count+=char

print(f'A in "{name}" is {len(count)} times')