# Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). 
# Write a program that calculates the slope of a line through two (non-vertical) points entered by the user.
#                    slope  =   y2 − y1
#                              ---------
#                               x2 − x1

def slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    
    return slope

print("A program that calculates slope of a line")
print()

# Get points coordinates
x1, y1 = eval(input("Enter the coordinates X1 and Y1 separated with a comma: "))
x2, y2 = eval(input("Enter the coordinates X2 and Y2 separated with a comma: "))

# Calculate and print slope
slope = slope(x1, y1, x2, y2)
print(f"The slope of the line through points ({x1}, {y1}) and ({x2}, {y2}) is {slope:.3f}")
