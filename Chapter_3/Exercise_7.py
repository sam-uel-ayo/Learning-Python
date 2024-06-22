# Write a program that accepts two points (see previous problem- Exercise_6.py) and determines the distance
#between them.
#                                    ----------------------------
#                   distance =     /  (x2 − x1)**2 + (y2 − y1)**2
#                                 v 

import math
def calculate_distance(x1, y1, x2, y2):
    # Calculate the distance using the distance formula
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

print("A program that calculates the distance of two points")
print()

# Get points coordinates
x1, y1 = eval(input("Enter the coordinates X1 and Y1 separated with a comma: "))
x2, y2 = eval(input("Enter the coordinates X2 and Y2 separated with a comma: "))


# Calculate and print distance
distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance of the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.3f}")
