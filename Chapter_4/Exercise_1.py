# 1. Alter the program from the last discussion question in the following ways:
#    (a) Make it draw squares instead of circles.
#    (b) Have each successive click draw an additional square on the screen (rather than moving
#        the existing one).
#    (c) Print a message on the window "Click again to quit" after the loop, and wait for a final
#        click before closing the window.

# Last discussion program
# from graphics import *
# def main():
#     win = GraphWin()
#     shape = Circle(Point(50,50), 20)
#     shape.setOutline("red")
#     shape.setFill("red")
#     shape.draw(win)
#     for i in range(10):
#         p = win.getMouse()
#         c = shape.getCenter()
#         dx = p.getX() - c.getX()
#         dy = p.getY() - c.getY()
#         shape.move(dx,dy)
#     win.close()
# main()


# 1(a)

from graphics import *
def main():
    win = GraphWin()
    shape = Rectangle(Point(40, 40), Point(60, 60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()
main()

# 1(b)

from graphics import *
def main():
    win = GraphWin()
    for i in range(10):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    win.close()
main()

# 1(c)

from graphics import *
def main():
    win = GraphWin()
    for i in range(10):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    
    message = Text(Point(win.getWidth()/2, win.getHeight()/2), "Click again to quit")
    message.draw(win)
    win.getMouse()  # Wait for final click
    win.close()
main()

