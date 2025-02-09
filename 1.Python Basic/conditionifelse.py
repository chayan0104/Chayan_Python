# Taking input from the user
age = int(input("Enter your age: "))

# Checking different age ranges and using 'not equals' condition
if age <= 13:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
elif age == 18:
    print("You are 18, great!")
elif age <= 30:
    print("You are a young adult.")
elif age >31 and age < 60:
    print("You are not that old, mate.")
elif age != 25:  # Special condition where age is not equal to 25
    print("You are not 25 yet!")
else:
    print("Happy retirement!")
