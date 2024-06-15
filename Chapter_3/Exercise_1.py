# Write a program to calculate the volume and surface area of a sphere from its radius, given
# as input. Here are some formulas that might be useful:
#                 V = 4/3πr**3
#                 A = 4πr**2

import math
def main():
    print("A program to calculate the volume and surface area of a sphere from its radius")
    print()
    
    # Get the radius from the user
    radius = float(input("What is the Radius of the sphere: "))
    volume = 4 / 3 * math.pi * pow(radius, 3)
    area = 4 * math.pi * pow(radius, 2)
    
    # Print the results with better formatting
    print(f"The Volume of the sphere is {volume:.2f}")
    print(f"The Surface Area of the sphere is {area:.2f}")
main()