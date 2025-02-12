from loguru import logger
employee_list = {
    "Mahesh": 500,
    "Rajesh": 600
}
employee_list["Sushil"] = 111 #adding to the dictionary

# Function to add in a particular position
def inser_at_position(person,cost,position):
    key =list(employee_list.keys())
    value=list(employee_list.values())

    key.insert(position,person)
    value.insert(position,cost)

    return dict(zip(key,value))

employee_list= inser_at_position("Sayam",100,0)

# Correct logger.info usage with formatting
logger.info("Cost: {}", employee_list)
print("Done added ")
