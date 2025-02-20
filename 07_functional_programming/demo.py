"""
land dimension = 100 x 100 ft | house dimension = 80 x 60 ft | garden dimension =100 x 20 ft

+-------------------------+
|    LAND (100 x 100)     |
|  +-------------------+  |
|  | HOUSE (80 x 60)   |  |
|-------------------------|
|    GARDEN (100 x 20)    |
+-------------------------+

cost for grass 10 rs/ft
"""
# Calculate area
def area(length, breadth):
    area = length * breadth
    return area

# Grass area
def grass_area(land_area, house_area, garden_area):
    total_grassing_area = land_area - (house_area + garden_area)
    return total_grassing_area

# Cost of Grassing
def cost_for_grass(cost_per_unit, total_grassing_area):
    total_cost_grassing = cost_per_unit * total_grassing_area
    return total_cost_grassing

# Data
land_area = area(100, 100)
house_area = area(80, 60)
garden_area = area(100, 20)
cost_per_unit = 10

# Calculate total grassing area
total_grassing_area = grass_area(land_area, house_area, garden_area)

# Calculate total cost for grassing
total_cost_grassing = cost_for_grass(cost_per_unit, total_grassing_area)

print("Total cost of grassing:", total_cost_grassing)
