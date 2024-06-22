# The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order
# ships for $0.86 per pound + $1.50 fixed cost for overhead. Write a program that calculates
# the cost of an order.The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order
# ships for $0.86 per pound + $1.50 fixed cost for overhead. Write a program that calculates
# the cost of an order.

def calculate_order_cost(pounds):
    # Constants
    price_per_pound = 10.50
    shipping_cost_per_pound = 0.86
    fixed_overhead_cost = 1.50
    
    # Calculate costs
    coffee_cost = pounds * price_per_pound
    shipping_cost = (pounds * shipping_cost_per_pound) + fixed_overhead_cost
    total_cost = coffee_cost + shipping_cost
    
    return total_cost

# Input: Number of pounds of coffee ordered
pounds = float(input("Enter the number of pounds of coffee ordered: "))

# Calculate and print the total cost
total_cost = calculate_order_cost(pounds)
print(f"The total cost of the order is ${total_cost:.2f}")
