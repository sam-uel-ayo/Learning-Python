# 2. An archery target consists of a central circle of yellow surrounded by concentric rings of red,
#    blue, black and white. Each ring has the same “width,” which is the same as the radius of
#    the yellow circle. Write a program that draws such a target. Hint: Objects drawn later will
#    appear on top of objects drawn earlier.

from graphics import *

def main():
    win = GraphWin("Archery Target", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    
    colors = ["white", "black", "blue", "red", "yellow"]
    radius = 10
    
    for color in colors:
        circle = Circle(Point(0, 0), radius)
        circle.setFill(color)
        circle.draw(win)
        radius -= 2

    win.getMouse()
    win.close()

main()

