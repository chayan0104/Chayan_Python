def calculate_total(discount, *prices, **extra_details):
    total = sum(prices)  # Summing up the prices
    print(f"Total cost before discount: {total}")
    
    # Applying the discount
    total_after_discount = total - (total * discount)
    print(f"Total cost after discount: {total_after_discount}")
    
    # Displaying extra details (using **kwargs)
    if extra_details:
        print("\nAdditional details:")
        for key, value in extra_details.items():
            print(f"{key}: {value}")

# Calling the function with both *args and **kwargs
calculate_total(0.1, 100, 200, 50, 30, description="Shopping Trip", store="SuperMart", offer="10% off")
