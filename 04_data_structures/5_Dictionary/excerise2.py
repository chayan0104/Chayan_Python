laborers = {
    1: {
        "name": "John Doe",
        "cost": 150,
        "address": "123 Maple Street",
        "id": "L001"
    },
    2: {
        "name": "Jane Smith",
        "cost": 120,
        "address": "456 Oak Avenue",
        "id": "L002"
    }
}

# Working days and leaves taken
total_work_days = 50
leave_days = {1: 3, 2: 7} #created another leave dictionary

# Calculate cost of project
total_cost = sum((total_work_days - leave_days[laborer_id]) * laborers[laborer_id]['cost'] 
                 for laborer_id in laborers)

print("Total project cost:", total_cost)
