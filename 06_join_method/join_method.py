
names=["Ram","Sam","Raj"]

joined_names = " ".join(names)

print(joined_names)
print("-".join(names))
print(",".join(names))
# --------------------------------------

numbers={1,2,3,4,6}

# map(function, iterable)
print(" ".join(map(str, numbers)))