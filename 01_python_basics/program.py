cost = 100
quantity = 5
total_cost = cost * quantity

# Simple
print("The cost is", cost, "per unit.Total cost for", quantity, "units is", total_cost, ".")

# F-string
print(f"The cost is {cost} per unit.Total cost for {quantity} units is {total_cost}.")

# .format
print("The cost is {} per unit.Total cost for {} units is {}.".format(cost, quantity, total_cost))
