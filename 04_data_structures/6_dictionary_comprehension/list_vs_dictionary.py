name="Manas"

letter_count={} #Dictionary

for char in name:
    if char in letter_count:
        letter_count[char] +=1
    else:
        letter_count[char] =1

print("Using dictionary:",letter_count)      
# ----------------------------------
name2 = "Manas"

letter_count = []
count = []

for char in name2:
    if char in letter_count:
        count[letter_count.index(char)] += 1
    else:
        letter_count.append(char)
        count.append(1)

print("Using list:",dict(zip(letter_count, count)))  # Convert to dictionary for display
