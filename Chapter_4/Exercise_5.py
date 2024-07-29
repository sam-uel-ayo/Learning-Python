# 5. Write a program that draws 5 dice on the screen depicting a straight (1, 2, 3, 4, 5 or 2, 3, 4, 5, 6).

from graphics import *

def draw_dice(win, center, value):
    size = 40
    half_size = size / 2
    die = Rectangle(Point(center.getX() - half_size, center.getY() - half_size),
                    Point(center.getX() + half_size, center.getY() + half_size))
    die.setFill("white")
    die.draw(win)
    
    pips = [(0, 0), (-15, -15), (15, 15), (-15, 15), (15, -15), (-15, 0), (15, 0), (0, -15), (0, 15)]
    
    pip_coords = []
    if value == 1:
        pip_coords = [pips[0]]
    elif value == 2:
        pip_coords = [pips[1], pips[2]]
    elif value == 3:
        pip_coords = [pips[0], pips[1], pips[2]]
    elif value == 4:
        pip_coords = [pips[1], pips[2], pips[3], pips[4]]
    elif value == 5:
        pip_coords = [pips[0], pips[1], pips[2], pips[3], pips[4]]
    elif value == 6:
        pip_coords = [pips[1], pips[2], pips[3], pips[4], pips[5], pips[6]]
    
    for coord in pip_coords:
        pip = Circle(Point(center.getX() + coord[0], center.getY() + coord[1]), 5)
        pip.setFill("black")
        pip.draw(win)

def main():
    win = GraphWin("Dice", 400, 200)
    
    for i in range(5):
        draw_dice(win, Point(60 + i * 80, 100), i + 1)
    
    win.getMouse()
    win.close()

main()

