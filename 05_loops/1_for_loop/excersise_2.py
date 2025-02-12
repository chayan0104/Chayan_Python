import logging
logging.basicConfig(level=logging.INFO)
para = """
The sun sets over the horizon, casting a warm, golden glow across the sky. 
Birds fly back to their nests as the cool evening breeze starts to flow. 
The world feels peaceful, with the soft sounds of nature all around. 
It's a moment to pause, reflect, and appreciate the simple beauty of the day.
"""

# print("original paragraph:", para)

para_list = para.upper().split()
# print("As list:",para_list)
total_letter=[]
for letter in para_list:
    if letter == "THE":
        total_letter.append(letter)
    else:
        continue    

# print("Total number of 'THE' in paragraph is",len(total_letter))  
logging.info(f"Total number of 'THE' in paragraph is {len(total_letter)}")      
        
        
        
