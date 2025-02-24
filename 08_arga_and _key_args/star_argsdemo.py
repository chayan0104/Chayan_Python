# star argument
def total_sum(discount, *cost):
    result = 0
    for price in cost:
        result += price
    
    print(f"Total amount is {result} rs")
    post_discount = result - (result * discount)
    return post_discount

amount_to_be_paid = total_sum(0.25, 10, 30, 20, 40)

print("Amount to be paid after discount",int(amount_to_be_paid),"rs")
