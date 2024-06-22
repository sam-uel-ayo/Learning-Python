# Write a program to calculate the area of a triangle given the length of its three sides a, b, and c 
# Using these formulas:
#                      S = (a + b + c)/2
#                             -----------------------
#                      A  =  / s(s − a)(s − b)(s − c)
#                           v
#

import math
def area_triangle(a, b, c):
    
    # Calculate s (semi-perimeter)
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    print("A program to calculate the area of a triangle")
    print()
    
    # Get length of sides of triangle
    a, b, c = eval(input("Enter length of the sides of triangle separated by a comma (a, b, c): "))
    
    area = area_triangle(a, b, c)
    
    print(f"The area of the triangle is {area:.2f}")

main()
