# Write a program that calculates the cost per square inch of a circular pizza, given its diameter
# and price. The formula for area is A = πr**2

import math
def main():
    print("A program that calculates the cost per square inch of a circular pizza")
    print()

    # Get the diameter and price of the pizza
    diameter = float(input("Enter the diameter of the pizza (in inches): "))
    price = float(input("Enter the price of the pizza (in dollars): "))

    # Calculate the radius and area
    radius = diameter / 2
    area = math.pi * pow(radius, 2)
    
    # Calculate the cost per square inch
    cost_per_square_inch = price / area

    # Print the cost per square inch
    print(f"The cost per square inch of the pizza is: ${cost_per_square_inch:.2f}")
main()
