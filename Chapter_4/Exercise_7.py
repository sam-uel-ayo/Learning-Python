# 7. Circle Intersection. Write a program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#     Input: Radius of the circle and the y-intercept of the line.
#     Output: - Draw a circle centered at (0, 0) with the given radius in a window with coordinates
#               running from -10,-10 to 10,10.
#             - Draw a horizontal line across the window with the given y-intercept.
#             - Draw the two points of intersection in red.
#     Print out the x values of the points of intersection.

from graphics import *
import math

def main():
    win = GraphWin("Circle Intersection", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    Text(Point(-5, 9), "Radius:").draw(win)
    radius_input = Entry(Point(0, 9), 5)
    radius_input.setText("5")
    radius_input.draw(win)
    
    Text(Point(-5, 8), "Y-Intercept:").draw(win)
    y_intercept_input = Entry(Point(0, 8), 5)
    y_intercept_input.setText("3")
    y_intercept_input.draw(win)
    
    Text(Point(0, -9), "Click to draw").draw(win)
    win.getMouse()
    
    radius = float(radius_input.getText())
    y_intercept = float(y_intercept_input.getText())
    
    circle = Circle(Point(0, 0), radius)
    circle.draw(win)
    
    line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    line.draw(win)
    
    if abs(y_intercept) <= radius:
        x = math.sqrt(radius**2 - y_intercept**2)
        intersec1 = Circle(Point(x, y_intercept), 0.2)
        intersec1.setFill("red")
        intersec1.draw(win)
        
        intersec2 = Circle(Point(-x, y_intercept), 0.2)
        intersec2.setFill("red")
        intersec2.draw(win)
        
        Text(Point(0, -8), f"Intersections: ±{x:.2f}").draw(win)
    else:
        Text(Point(0, -8), "No intersection").draw(win)
    
    win.getMouse()
    win.close()

main()

