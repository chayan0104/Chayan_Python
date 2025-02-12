import time

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# index = 0
index = len(names)-1  #3

# while index < len(names):
while index >= 0:
    print(names[index])
    time.sleep(2) # Sleep in output 
    # index += 1  # Increment the index to move to the next name
    index -=1  # Will print inverted list 

print("All names have been printed.")
