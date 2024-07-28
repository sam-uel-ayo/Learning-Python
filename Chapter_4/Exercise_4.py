# 4. Write a program that draws a winter scene with a Christmas tree and a snowman.

from graphics import *

def main():
    win = GraphWin("Winter Scene", 400, 400)
    
    # Snowman
    base = Circle(Point(200, 300), 50)
    base.setFill("white")
    base.draw(win)
    
    mid = Circle(Point(200, 220), 35)
    mid.setFill("white")
    mid.draw(win)
    
    head = Circle(Point(200, 160), 25)
    head.setFill("white")
    head.draw(win)
    
    # Eyes
    left_eye = Circle(Point(190, 150), 5)
    left_eye.setFill("black")
    left_eye.draw(win)
    
    right_eye = Circle(Point(210, 150), 5)
    right_eye.setFill("black")
    right_eye.draw(win)
    
    # Nose
    nose = Polygon(Point(200, 160), Point(200, 170), Point(220, 165))
    nose.setFill("orange")
    nose.draw(win)
    
    # Christmas Tree
    trunk = Rectangle(Point(50, 300), Point(70, 350))
    trunk.setFill("brown")
    trunk.draw(win)
    
    leaves1 = Polygon(Point(30, 300), Point(60, 200), Point(90, 300))
    leaves1.setFill("green")
    leaves1.draw(win)
    
    leaves2 = Polygon(Point(35, 250), Point(60, 150), Point(85, 250))
    leaves2.setFill("green")
    leaves2.draw(win)
    
    leaves3 = Polygon(Point(40, 200), Point(60, 100), Point(80, 200))
    leaves3.setFill("green")
    leaves3.draw(win)
    
    win.getMouse()
    win.close()

main()
