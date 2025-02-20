"""
def function_name (Arguments)
example: "def house_cost(length,breadth,cost):"
Positinal Arguments :- length(1),breadth(2),cost(3)--(will be considered as vaiables)
"""

# function to calculate the cost of a house
def house_cost(length, breadth, cost):
    area = length * breadth
    total_cost = area * cost
    
    return total_cost

print("Total cost of making the house :",house_cost(22,12,50))