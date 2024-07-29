# 11. Five-click house.
#     You are to write a program that allows the user to draw a simple house using five mouseclicks. The first two clicks will be the opposite corners of the rectangular frame of the house.
#     The third click will indicate the center of the top edge of a rectangular door. The door should
#     have a total width that is 1/5 of the width of the house frame. The sides of the door should
#     extend from the corners of the top down to the bottom of the frame. The fourth click will
#     indicate the center of a square window. The window is half as wide as the door. The last click
#     will indicate the peak of the roof. The edges of the roof will extend from the point at the peak
#     to the corners of the top edge of the house frame

from graphics import *

def main():
    win = GraphWin("Five-Click House", 400, 400)
    
    Text(Point(200, 50), "Click on two points for the corners of the house").draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    
    house = Rectangle(p1, p2)
    house.draw(win)
    
    width = abs(p2.getX() - p1.getX())
    door_width = width / 5
    Text(Point(200, 70), "Click for the top center of the door").draw(win)
    door_center = win.getMouse()
    
    door = Rectangle(Point(door_center.getX() - door_width / 2, p1.getY()),
                Point(door_center.getX() + door_width / 2, door_center.getY()))
    door.draw(win)
    
    window_width = door_width / 2
    Text(Point(200, 90), "Click for the center of the window").draw(win)
    window_center = win.getMouse()
    
    window = Rectangle(Point(window_center.getX() - window_width / 2, window_center.getY() - window_width / 2),
                Point(window_center.getX() + window_width / 2, window_center.getY() + window_width / 2))
    window.draw(win)
    
    Text(Point(200, 110), "Click for the peak of the roof").draw(win)
    peak = win.getMouse()
    
    roof = Polygon(Point(p1.getX(), p2.getY()), Point(p2.getX(), p2.getY()), peak)
    roof.draw(win)
    
    win.getMouse()
    win.close()

main()
